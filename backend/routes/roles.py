from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from backend.composables.decorators.role_verification import allows
from backend.composables.decorators.validate_parameters import validate_parameters, Route, Json

from backend.services.role_service import role_service


# required line at the top of every blueprint file
roles = Blueprint("roles", __name__)

# all
@roles.get('/')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def get_roles():
    return role_service.get_roles()

# create
@roles.post('/')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def create_role(name: str = Json()):
    return role_service.create_role(name)

# read
@roles.get('/<int:role_id>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def get_role(role_id: int = Route()):
    return role_service.get_role(role_id)

# update
@roles.patch('/<int:role_id>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def update_role(role_id: int = Route(), name: str = Json()):
    return role_service.update_role(role_id, name)

# delete
@roles.delete('/<int:role_id>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def delete_role(role_id: int = Route()):
    return role_service.delete_role(role_id)
