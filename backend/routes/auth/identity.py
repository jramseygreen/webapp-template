from typing import Optional
from flask import Blueprint
from flask_jwt_extended import jwt_required

from backend.composables.decorators.validate_parameters import validate_parameters, Json

from backend.services.auth.identity_service import identity_service


identity = Blueprint("identity", __name__)


@identity.post('/')
@validate_parameters()
def create_identity(
    username: str = Json(),
    password: str = Json()
):
    return identity_service.create_identity(username, password)


@identity.get('/')
@jwt_required()
@validate_parameters()
def get_identity():
    return identity_service.get_identity()


@identity.patch('/')
@jwt_required()
@validate_parameters()
def update_identity(password: str = Json(), username: Optional[str] = Json(default=None), new_password: Optional[str] = Json(default=None)):
    return identity_service.update_identity(username=username, password=password, new_password=new_password)


@identity.delete('/')
@jwt_required()
@validate_parameters()
def delete_identity(password: str = Json()):
    return identity_service.delete_identity(password)
