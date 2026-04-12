from flask import Blueprint, current_app
from flask_jwt_extended import jwt_required
from controllers.note_controller import list_notes, create_note, update_note, delete_note, get_note

note_bp = Blueprint('note', __name__)

@note_bp.route('/', methods=['GET'])
@jwt_required()
def notes():
    return list_notes(current_app)

@note_bp.route('/', methods=['POST'])
@jwt_required()
def add_note():
    return create_note(current_app)

@note_bp.route('/<note_id>', methods=['GET'])
@jwt_required()
def fetch_note(note_id):
    return get_note(current_app, note_id)

@note_bp.route('/<note_id>', methods=['PUT'])
@jwt_required()
def edit_note(note_id):
    return update_note(current_app, note_id)

@note_bp.route('/<note_id>', methods=['DELETE'])
@jwt_required()
def remove_note(note_id):
    return delete_note(current_app, note_id)
