import bcrypt
from bson.errors import InvalidId
from bson.objectid import ObjectId
from flask import jsonify


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


def parse_object_id(value: str, field_name: str = 'id'):
    try:
        return ObjectId(value)
    except (InvalidId, TypeError):
        return None


def resp(success: bool, message: str, data=None, status=200):
    body = {'success': success, 'message': message}
    if data is not None:
        body['data'] = data
    return jsonify(body), status
