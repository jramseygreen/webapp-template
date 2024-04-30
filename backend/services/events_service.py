from flask_jwt_extended import current_user, get_jwt

from backend.composables.response import response

from backend.controllers.events_controller import events_controller
from backend.controllers.auth_controller import auth_controller

class __EventsService:
    def listen(self):
        jwt = get_jwt()
        auth_controller.blacklist_jwt(jwt)
        return events_controller.listen(current_user.id)

    def generate_access_token(self):
        access_token = events_controller.generate_access_token(current_user)
        return response.created("Temporary token created successfully", {'token': access_token})

events_service = __EventsService()
