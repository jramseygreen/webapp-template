from flask_jwt_extended import current_user, get_jwt

from backend.composables.response import response

from backend.controllers.auth_controller import auth_controller
from backend.controllers.user_controller import user_controller

class __AuthService:
    def login(self, username: str, password: str, remember_me: bool):
        tokens = auth_controller.login(username, password, remember_me)
        if tokens:
            return response.ok('Logged in successfully', tokens)
        return response.unauthorized('Incorrect username or password')

    def refresh(self):
        token = auth_controller.refresh(current_user)
        if token:
            return response.ok('Token refreshed successfully', token)
        return response.unauthorized('Invalid credentials for token refresh')

    def blacklist_token(self):
        jwt = get_jwt()
        success = auth_controller.blacklist_token(jwt)
        if success:
            return response.ok('blacklisted token successfully')
        return response.internal_server_error('Token already blacklisted')


auth_service = __AuthService()
