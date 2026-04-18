from flask import Blueprint, current_app
from flask_jwt_extended import jwt_required
from controllers.task_controller import list_tasks, create_task, update_task, delete_task

task_bp = Blueprint('task', __name__)

@task_bp.route('/', methods=['GET'])
@jwt_required()
def tasks():
    return list_tasks(current_app)

@task_bp.route('/', methods=['POST'])
@jwt_required()
def add_task():
    return create_task(current_app)

@task_bp.route('/<task_id>', methods=['PUT'])
@jwt_required()
def edit_task(task_id):
    return update_task(current_app, task_id)

@task_bp.route('/<task_id>', methods=['DELETE'])
@jwt_required()
def remove_task(task_id):
    return delete_task(current_app, task_id)
