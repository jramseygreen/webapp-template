from flask import Blueprint, jsonify
from typing import Optional
from flask_jwt_extended import jwt_required

from backend.composables.decorators.validate_parameters import validate_parameters, Route, Json
from backend.composables.decorators.role_verification import allows
from backend.services.settings_service import settings_service

settings = Blueprint("settings", __name__)

# all
@settings.get('/')
def get_settings():
    return settings_service.get_settings()

# read
@settings.get('/<string:name>')
@validate_parameters()
def get_setting(name: str = Route()):
    return settings_service.get_setting(name)

# update
@settings.patch('/<string:name>')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def update_setting(name: str = Route(), value: Optional[str] = Json(default=None), description: Optional[str] = Json(default=None)):
    return settings_service.update_setting(name, value, description)

@settings.patch('/')
@jwt_required()
@validate_parameters()
@allows(admin=True)
def update_all_settings(settings: list = Json()):
    return settings_service.update_all_settings(settings)
