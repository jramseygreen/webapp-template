from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime

from backend.db import db

from backend.models.user import User
from backend.models.token_blocklist import TokenBlocklist

class __AuthController:
    def login(self, username: str, password: str, remember_me: bool) -> dict:
        # Check if the user exists in the database
        user = db.session.query(User).filter_by(username=username).one_or_none()

        if not user or not user.check_password(password) or user.is_disabled:
            return

        payload = {
            'token': create_access_token(identity=user),
            'refresh_token': None
        }
        if remember_me:
            payload['refresh_token'] = create_refresh_token(identity=user)

        return payload

    def blacklist_token(self, jwt: dict):
        jti = jwt['jti']
        if TokenBlocklist.is_jti_blacklisted(jti):
            return False

        expires = jwt['exp']
        db.session.add(TokenBlocklist(jti=jti, expires_at=datetime.fromtimestamp(expires)))
        db.session.commit()
        return True

    def refresh(self, identity: User) -> dict:
        return {
            'token': create_access_token(identity=identity)
        }

auth_controller = __AuthController()
