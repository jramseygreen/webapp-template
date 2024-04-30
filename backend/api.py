from flask import Blueprint, jsonify
from .routes.users import users
from .routes.auth.auth import auth
from .routes.roles import roles
from .routes.events import events
from .routes.settings import settings
from flask_parameter_validation.docs_blueprint import docs_blueprint

# required line at the top of every blueprint file
api = Blueprint("api", __name__)  # match variable name and first arg to file name
# register more blueprints here to further split up the api
# e.g.
# api.register_blueprint(blueprint, url_prefix='/users')
# would cascade through /api/users

api.register_blueprint(docs_blueprint, url_prefix="") # generated api documentation on '/' and '/json'
api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(auth, url_prefix="/auth")
api.register_blueprint(roles, url_prefix="/roles")
api.register_blueprint(events, url_prefix="/events")
api.register_blueprint(settings, url_prefix="/settings")

# api routes when hitting /api
@api.get("/status")
def heartbeat():
    return jsonify({"status": "healthy"})
