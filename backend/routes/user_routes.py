from flask import Blueprint, current_app
from flask_jwt_extended import jwt_required
from controllers.user_controller import get_profile, update_profile, change_password, get_user_stats

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return get_profile(current_app)

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def edit_profile():
    return update_profile(current_app)

@user_bp.route('/change-password', methods=['POST'])
@jwt_required()
def pwd_change():
    return change_password(current_app)

@user_bp.route('/stats', methods=['GET'])
@jwt_required()
def stats():
    return get_user_stats(current_app)
