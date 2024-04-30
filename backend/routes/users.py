from flask import Blueprint, jsonify
from typing import List, Optional
from flask_jwt_extended import jwt_required

from backend.composables.decorators.validate_parameters import validate_parameters, Route, Json, Query
from backend.composables.decorators.role_verification import allows, blocks

from backend.services.user_service import user_service


# required line at the top of every blueprint file
users = Blueprint("users", __name__)  # match variable name and first arg to file name
# register more blueprints here to further split up the api
# e.g.
# api.register_blueprint(blueprint, url_prefix='/users')
# would cascade through /api/users

# all
@users.get('/')
@jwt_required()
@allows(admin=True)
def get_users():
    return user_service.get_users()


# create
@users.post('/')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def create_user(username: str = Json(), password: str = Json(), is_disabled: Optional[bool] = Json(default=False), roles: Optional[List[str]] = Json(default=None)):
    return user_service.create_user(username, password, is_disabled, roles)


#read
@users.get('/<int:user_id>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def get_user(user_id: int = Route()):
    return user_service.get_user(user_id)

# update
@users.patch('/<int:user_id>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def update_user(user_id: int = Route(), username: Optional[str] = Json(default=None), password: Optional[str] = Json(default=None), is_disabled: Optional[bool] = Json(default=None), roles: Optional[List[str]] = Json(default=None)):
    return user_service.update_user(user_id, username, password, is_disabled, roles)


# delete
@users.delete('/<int:user_id>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def delete_user(user_id: int = Route()):
    return user_service.delete_user(user_id)
