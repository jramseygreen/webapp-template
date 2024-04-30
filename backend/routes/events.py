from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from backend.composables.sse import sse
from backend.composables.decorators.role_verification import allows, blocks

from backend.services.events_service import events_service

# required line at the top of every blueprint file
events = Blueprint("events", __name__)  # match variable name and first arg to file name


# if you wanted you could supply a unique id to the listen method to send messages to specific clients
# must pass jwt in query param
@events.get("/listen")
@jwt_required(fresh=True)
def listen():
  return events_service.listen()

@events.get("/access-token")
@jwt_required()
def generate_access_token():
    return events_service.generate_access_token()
