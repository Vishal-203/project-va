from flask import Blueprint, current_app
from flask_jwt_extended import jwt_required
from controllers.share_controller import share_note, unshare_note, get_shared_notes, get_note_shares

share_bp = Blueprint('share', __name__)


@share_bp.route('/<note_id>/share', methods=['POST'])
@jwt_required()
def add_share(note_id):
    return share_note(current_app, note_id)


@share_bp.route('/<note_id>/share/<share_user_id>', methods=['DELETE'])
@jwt_required()
def remove_share(note_id, share_user_id):
    return unshare_note(current_app, note_id, share_user_id)


@share_bp.route('/shared', methods=['GET'])
@jwt_required()
def shared():
    return get_shared_notes(current_app)


@share_bp.route('/<note_id>/shares', methods=['GET'])
@jwt_required()
def shares(note_id):
    return get_note_shares(current_app, note_id)
