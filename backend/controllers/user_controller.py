from typing import List, Optional

from backend.db import db
from backend.models.user import User
from backend.controllers.role_controller import role_controller

class __UserController:
    # all
    def get_users(self) -> List[User]:
        # Get all users
        query = db.session.query(User)

        # Execute the query and return the results
        users = query.all()
        return users

    # create
    def create_user(self, username: str, password: str, is_disabled: bool = False, roles: Optional[List[str]] = []) -> Optional[User]:
        # Create a new user
        existing_user = db.session.query(User).filter_by(username=username).first()
        if not existing_user:
            new_user = User(username=username, is_disabled=is_disabled)
            new_user.set_password(password)
            if roles is not None:
                new_user.roles = role_controller.get_roles(role_names=roles)
            db.session.add(new_user)
            db.session.commit()
            return new_user

    # read
    def get_user(self, user_id: int) -> Optional[User]:
        # Get a specific user by user_id
        user = db.session.query(User).get(user_id)
        if user:
            return user

    # update
    def update_user(self, user_id: int, username: str = None, password: str = None, is_disabled: bool = None, roles: Optional[List[str]] = None) -> Optional[User]:
        # Update a specific user by user_id
        user = db.session.query(User).get(user_id)
        if user:
            if username:
                user.username = username
            if password:
                user.set_password(password)
            if is_disabled is not None:
                user.is_disabled = is_disabled
            if roles is not None:
                user.roles = role_controller.get_roles(role_names=roles)
            db.session.commit()
            return user

    # delete
    def delete_user(self, user_id: int) -> bool:
        # Delete a specific user by user_id
        user = db.session.query(User).get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

user_controller = __UserController()
