from flask import Blueprint
from flask_jwt_extended import jwt_required
from .identity import identity

from backend.composables.decorators.validate_parameters import validate_parameters, Route, Json, Query

from backend.services.auth.auth_service import auth_service


# required line at the top of every blueprint file
auth = Blueprint("auth", __name__)  # match variable name and first arg to file name

auth.register_blueprint(identity, url_prefix='/identity')

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@auth.post('/login')
@validate_parameters()
def login(
    username: str = Json(),
    password: str = Json(),
    remember_me: bool = Json()
):
    return auth_service.login(username, password, remember_me)

@auth.delete('/blacklist-token')
@jwt_required()
def blacklist_token():
    return auth_service.blacklist_token()

@auth.delete('/blacklist-refresh-token')
@jwt_required(refresh=True)
def blacklist_refresh_token():
    return auth_service.blacklist_token()

@auth.post('/refresh')
@jwt_required(refresh=True)
@validate_parameters()
def refresh():
    return auth_service.refresh()
