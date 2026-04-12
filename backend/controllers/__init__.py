"""
Controllers package - business logic layer
"""
from .auth_controller import register_user, login_user, profile
from .note_controller import list_notes, create_note, update_note, delete_note, get_note
from .task_controller import list_tasks, create_task, update_task, delete_task
from .ai_controller import answer_question, summarize_text, generate_quiz
from .user_controller import get_profile, update_profile, change_password, get_user_stats
from .share_controller import share_note, unshare_note, get_shared_notes, get_note_shares
from .file_controller import upload_file, delete_file, get_file, list_files

__all__ = [
    'register_user', 'login_user', 'profile',
    'list_notes', 'create_note', 'update_note', 'delete_note', 'get_note',
    'list_tasks', 'create_task', 'update_task', 'delete_task',
    'answer_question', 'summarize_text', 'generate_quiz',
    'get_profile', 'update_profile', 'change_password', 'get_user_stats',
    'share_note', 'unshare_note', 'get_shared_notes', 'get_note_shares',
    'upload_file', 'delete_file', 'get_file', 'list_files'
]
