from backend.composables.response import response

from backend.controllers.role_controller import role_controller

class __RoleService:
    # all
    def get_roles(self):
        roles = role_controller.get_roles()
        return response.ok('Retrieved all roles successfully', [role.to_dict() for role in roles])

    # create
    def create_role(self, name: str):
        role = role_controller.create_role(name)
        if role:
            return response.created("Role created successfully", role.to_dict())
        return response.bad_request("Role already exists")

    # read
    def get_role(self, role_id: int):
        role = role_controller.get_role(role_id)
        if role:
            return response.ok('Retrieved role successfully', role.to_dict())
        return response.not_found('Role not found')

    # update
    def update_role(self, role_id: int, name: str):
        role_to_update = role_controller.get_role(role_id)
        if role_to_update and role_to_update.name == 'admin':
            return response.method_not_allowed('Admin role cannot be modified')

        role = role_controller.update_role(role_id, name)
        if role:
            return response.ok("Role updated successfully", role.to_dict())
        return response.not_found("Role not found")

    # delete
    def delete_role(self, role_id: int):
        role_to_delete = role_controller.get_role(role_id)
        if role_to_delete and role_to_delete.name == 'admin':
            return response.method_not_allowed('Admin role cannot be deleted')

        is_deleted = role_controller.delete_role(role_id)
        if is_deleted:
            return response.ok("Role deleted successfully")
        return response.not_found("Role not found")

role_service = __RoleService()
