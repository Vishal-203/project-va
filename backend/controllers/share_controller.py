from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.helpers import parse_object_id, resp


@jwt_required()
def share_note(app, note_id):
    """Share note with another user"""
    user_id = get_jwt_identity()
    note_obj_id = parse_object_id(note_id, 'note_id')
    if note_obj_id is None:
        return resp(False, 'Invalid note ID', status=400)

    data = request.get_json() or {}
    shared_email = data.get('email', '').strip().lower()
    
    if not shared_email:
        return resp(False, 'Email is required', status=400)
    
    # Get note
    note = app.mongo.db.notes.find_one({'_id': note_obj_id, 'user_id': user_id})
    if not note:
        return resp(False, 'Note not found', status=404)
    
    # Find user by email
    shared_user = app.mongo.db.users.find_one({'email': shared_email})
    if not shared_user:
        return resp(False, 'User not found', status=404)
    
    # Prevent sharing with self
    if str(shared_user['_id']) == user_id:
        return resp(False, 'Cannot share with yourself', status=400)
    
    shared_user_id = str(shared_user['_id'])
    
    # Check if already shared
    if not note.get('shared_with'):
        shared_list = []
    else:
        shared_list = note['shared_with']
    
    if shared_user_id in shared_list:
        return resp(False, 'Already shared with this user', status=409)
    
    # Add to shared list
    shared_list.append(shared_user_id)
    app.mongo.db.notes.update_one(
        {'_id': note_obj_id},
        {'$set': {'shared_with': shared_list}}
    )
    
    return resp(True, f'Note shared with {shared_email}')


@jwt_required()
def unshare_note(app, note_id, share_user_id):
    """Revoke note sharing"""
    user_id = get_jwt_identity()
    note_obj_id = parse_object_id(note_id, 'note_id')
    if note_obj_id is None:
        return resp(False, 'Invalid note ID', status=400)
    
    # Get note
    note = app.mongo.db.notes.find_one({'_id': note_obj_id, 'user_id': user_id})
    if not note:
        return resp(False, 'Note not found', status=404)
    
    # Remove from shared list
    shared_list = note.get('shared_with', [])
    if share_user_id not in shared_list:
        return resp(False, 'Not shared with this user', status=404)
    
    shared_list.remove(share_user_id)
    app.mongo.db.notes.update_one(
        {'_id': note_obj_id},
        {'$set': {'shared_with': shared_list}}
    )
    
    return resp(True, 'Sharing revoked')


@jwt_required()
def get_shared_notes(app):
    """Get notes shared with current user (read-only)"""
    user_id = get_jwt_identity()
    
    # Find notes where user_id is in shared_with array
    shared_notes = list(app.mongo.db.notes.find({
        'shared_with': user_id
    }).sort('updated_at', -1))
    
    for note in shared_notes:
        note['id'] = str(note['_id'])
        note.pop('_id', None)
        note['is_shared'] = True
        note['is_owner'] = False
    
    return resp(True, 'Shared notes fetched', shared_notes)


@jwt_required()
def get_note_shares(app, note_id):
    """Get list of users note is shared with"""
    user_id = get_jwt_identity()
    note_obj_id = parse_object_id(note_id, 'note_id')
    if note_obj_id is None:
        return resp(False, 'Invalid note ID', status=400)
    
    # Get note
    note = app.mongo.db.notes.find_one({'_id': note_obj_id, 'user_id': user_id})
    if not note:
        return resp(False, 'Note not found', status=404)
    
    shared_user_ids = note.get('shared_with', [])
    
    # Get user details for each shared user
    shared_users = []
    for shared_id in shared_user_ids:
        shared_obj_id = parse_object_id(shared_id, 'shared_user_id')
        if shared_obj_id is None:
            continue

        user = app.mongo.db.users.find_one(
            {'_id': shared_obj_id},
            {'password': False}
        )
        if user:
            shared_users.append({
                'id': str(user['_id']),
                'name': user.get('name', 'Unknown'),
                'email': user.get('email', 'unknown@example.com')
            })
    
    return resp(True, 'Shares fetched', shared_users)
