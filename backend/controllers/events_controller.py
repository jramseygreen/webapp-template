from flask_jwt_extended import create_access_token
from datetime import timedelta

from backend.composables.sse import sse

from backend.models.user import User

from flask import Response

class __EventsController:
    def listen(self, user_id: int) -> Response:
        stream = sse.listen(user_id)
        return stream

    def generate_access_token(self, identity: User) -> str:
        expires = timedelta(minutes=1)  # Set the expiration time to 1 minute
        access_token = create_access_token(identity=identity, expires_delta=expires, fresh=True)
        return access_token

events_controller = __EventsController()
