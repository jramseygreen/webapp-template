from typing import Optional, List
from backend.composables.response import response

from backend.controllers.user_controller import user_controller

class __UserService:
    # all
    def get_users(self):
        users = user_controller.get_users()
        return response.ok('Retrieved all users successfully', [user.to_dict() for user in users])

    # create
    def create_user(self, username: str, password: str, is_disabled: Optional[bool], roles: Optional[List[str]]):
        user = user_controller.create_user(username=username, password=password, is_disabled=is_disabled, roles=roles)
        if user:
            return response.created("User created successfully", user.to_dict())
        return response.bad_request("Username already exists")

    # read
    def get_user(self, user_id: int):
        # Get a specific user by user_id
        user = user_controller.get_user(user_id)
        if user:
            return response.ok('Retrieved user successfully', user.to_dict())
        return response.not_found('User not found')

    # update
    def update_user(self, user_id: int, username: Optional[str], password: Optional[str], is_disabled: Optional[bool], roles: Optional[List[str]]):
        # Update a specific user by user_id
        user = user_controller.update_user(user_id, username=username, password=password, is_disabled=is_disabled, roles=roles)
        if user:
            return response.ok("User updated successfully", user.to_dict())
        return response.not_found("User not found")

    # delete
    def delete_user(self, user_id: int):
        # Delete a specific user by user_id
        is_deleted = user_controller.delete_user(user_id)
        if is_deleted:
            return response.ok("User deleted successfully")
        return response.not_found("User not found")

user_service = __UserService()
