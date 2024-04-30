from flask import Flask, request, abort
from flask_migrate import Migrate, upgrade
from flask_jwt_extended import JWTManager, current_user, jwt_required

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime, timedelta

from backend.db import db
from backend.composables.response import response

from backend.models.user import User
from backend.models.setting import Setting
from backend.models.token_blocklist import TokenBlocklist


def setup_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    migrate = Migrate(app, db, command='db', directory='backend/migrations')

def run_migrations(app: Flask):
    # run all migrations
    with app.app_context():
        upgrade(revision='head')

def setup_jwt(app: Flask):
    # set secret key from database
    # randomised key is set during migrations
    with app.app_context():
        jwt_secret_key = db.session.query(Setting).get("JWT_SECRET_KEY")
        app.config["JWT_SECRET_KEY"] = jwt_secret_key.get_value()
        app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']  # Accept tokens from both header and query string
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
        app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=20)

    # this function and the scheduler below are responsible for garbage collection on expired tokens which have been revoked
    def __remove_expired_tokens():
        with app.app_context():
            expired_tokens = db.session.query(TokenBlocklist).filter(TokenBlocklist.expires_at <= datetime.utcnow())
            expired_tokens.delete()
            db.session.commit()

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=__remove_expired_tokens, trigger="interval", hours=8)
    scheduler.start()
    # Registering shutdown function
    atexit.register(lambda: scheduler.shutdown())

    jwt = JWTManager(app)

    # pass in user model and return the id to be embedded as jwt_identity
    @jwt.user_identity_loader
    def user_identity_lookup(user: User) -> int:
        return user.id

    # this returns the user object when getting the jwt_current_user
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data) -> User:
        identity = jwt_data["sub"]
        return db.session.query(User).filter_by(id=identity).one_or_none()

    # override when no jwt token is present
    @jwt.unauthorized_loader
    def unauthorized(message):
        return response.unauthorized('You must be logged in to see this resource', error_type='jwt_required')

    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        return response.unauthorized('Login has expired', error_type='jwt_expired')

    @jwt.token_verification_failed_loader
    def token_verification_failed(jwt_header, jwt_payload):
        return response.unauthorized('Could not verify login token', error_type='jwt_verification_failed')

    @jwt.invalid_token_loader
    def invalid_token(message):
        return response.unauthorized('Login token is invalid', error_type='jwt_invalid')

    @jwt.revoked_token_loader
    def add_token_to_blocklist(jwt_header, jwt_payload):
        return response.unauthorized('Login token revoked', error_type='jwt_revoked')

    @jwt.needs_fresh_token_loader
    def add_token_to_blocklist(jwt_header, jwt_payload):
        return response.unauthorized('The token to access this resource must be fresh', error_type='jwt_fresh')

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return TokenBlocklist.is_jti_blacklisted(jti)

def setup_request_handling(app: Flask, base_url: str):
    @app.before_request
    def before_request_func():
        path = request.path
        if path.startswith(base_url) and path[-1] != '/':
            # test()
            # provide user access override
            # abort(response.ok('test'))
            # allow users and admins to access

            # overrides = db.query(AccessPaths).match(path=path)
            # do kicking logic
            pass
