import os

from flask import request
from flask_jwt_extended import jwt_required
from openai import OpenAI

from controllers.file_analyzer import extract_text_from_file
from utils.helpers import resp


def get_ai_client():
    api_key = os.getenv('OPENAI_API_KEY', '').strip()
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def get_ai_model():
    return os.getenv('OPENAI_MODEL', 'gpt-4o-mini').strip() or 'gpt-4o-mini'


def _build_question_prompt(question, file_text=None):
    if file_text:
        return (
            'Use the following document text to answer the question. '\
            'If the document text is not needed, answer based on your knowledge and the question.\n\n'
            'Document text:\n' + file_text + '\n\n' +
            'Question:\n' + question
        )
    return question


def _build_summary_prompt(text):
    return (
        'Summarize the following text in 3-4 bullet points, keeping the summary clear and concise.\n\n' +
        text
    )


@jwt_required()
def answer_question(app):
    data = request.get_json() or {}
    question = data.get('question', '').strip()
    file_id = data.get('file_id')
    if not question:
        return resp(False, 'Question is required', status=400)

    file_text = None
    if file_id:
        file_result = extract_text_from_file(app, file_id)
        if not file_result.get('success'):
            return resp(False, file_result.get('message', 'File extraction failed'), status=file_result.get('status', 400))
        file_text = file_result['data']['text']

    client = get_ai_client()
    if client is None:
        return resp(False, 'AI service is not configured', status=503)

    try:
        prompt = _build_question_prompt(question, file_text)
        response = client.chat.completions.create(
            model=get_ai_model(),
            messages=[
                {'role': 'system', 'content': 'You are a helpful academic assistant. Answer questions concisely and clearly.'},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=400,
            temperature=0.7
        )
        ans = response.choices[0].message.content.strip()
        return resp(True, 'Answer generated', {'answer': ans})
    except Exception as e:
        return resp(False, f'AI service error: {str(e)}', status=500)


@jwt_required()
def summarize_text(app):
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    file_id = data.get('file_id')

    if file_id:
        file_result = extract_text_from_file(app, file_id)
        if not file_result.get('success'):
            return resp(False, file_result.get('message', 'File extraction failed'), status=file_result.get('status', 400))
        text = file_result['data']['text']

    if not text:
        return resp(False, 'Text or file_id is required', status=400)

    client = get_ai_client()
    if client is None:
        return resp(False, 'AI service is not configured', status=503)

    try:
        prompt = _build_summary_prompt(text)
        response = client.chat.completions.create(
            model=get_ai_model(),
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant. Summarize the given text in 3-4 bullet points.'},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        summary = response.choices[0].message.content.strip()
        return resp(True, 'Summary generated', {'summary': summary})
    except Exception as e:
        return resp(False, f'AI service error: {str(e)}', status=500)


@jwt_required()
def generate_quiz(app):
    data = request.get_json() or {}
    topic = data.get('topic', '').strip()
    if not topic:
        return resp(False, 'Topic is required', status=400)

    client = get_ai_client()
    if client is None:
        return resp(False, 'AI service is not configured', status=503)

    try:
        response = client.chat.completions.create(
            model=get_ai_model(),
            messages=[
                {'role': 'system', 'content': 'You are an educational assistant. Create a 5-question academic quiz with answers for the given topic.'},
                {'role': 'user', 'content': f'Create a quiz on: {topic}'}
            ],
            max_tokens=500,
            temperature=0.6
        )
        quiz = response.choices[0].message.content.strip()
        return resp(True, 'Quiz generated', {'quiz': quiz})
    except Exception as e:
        return resp(False, f'AI service error: {str(e)}', status=500)
