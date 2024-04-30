from flask_jwt_extended import current_user

from backend.composables.response import response

from backend.controllers.user_controller import user_controller
from backend.controllers.settings_controller import settings_controller

class __IdentityService:
    def create_identity(self, username: str, password: str):
        registration_enabled = settings_controller.get_setting('REGISTRATION_ENABLED')
        if registration_enabled and registration_enabled.get_value():
            created_user = user_controller.create_user(username=username, password=password)
            if created_user:
                return response.created('Registered user successfully')
            return response.bad_request('User already exists')
        return response.bad_request('User registration is disabled')

    def get_identity(self):
        return response.ok('Retrieved identity successfully', current_user.to_dict())

    def update_identity(self, username: str, password: str, new_password: str):
        if current_user.check_password(password):
            user = user_controller.update_user(current_user.id, username=username, password=new_password)
            if user:
                return response.ok('User updated successfully', user.to_dict())
            return response.bad_request('User does not exist')
        return response.bad_request('Password incorrect')

    def delete_identity(self, password: str):
        if current_user.check_password(password):
            user = user_controller.delete_user(current_user.id)
            if user:
                return response.ok('User deleted successfully')
            return response.bad_request('User does not exist')
        return response.bad_request('Password incorrect')

identity_service = __IdentityService()
