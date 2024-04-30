from typing import Optional, List

from backend.db import db
from backend.models.role import Role

class __RoleController:
    # all
    def get_roles(self, role_names: Optional[List[str]] = None) -> List[Role]:
        # Get all roles
        query = db.session.query(Role)

        # Filter the query if a list of role names is provided
        if role_names is not None:
            query = query.filter(Role.name.in_(role_names))

        # Execute the query and return the results
        roles = query.all()
        return roles

    # create
    def create_role(self, name: str) -> Optional[Role]:
        # Create a new role
        existing_role = db.session.query(Role).filter_by(name=name).one_or_none()
        if not existing_role:
            new_role = Role(name=name)
            db.session.add(new_role)
            db.session.commit()
            return new_role

    # read
    def get_role(self, role_id: int) -> Optional[Role]:
        # Get a specific role by role_id
        role = db.session.query(Role).get(role_id)
        if role:
            return role

    # update
    def update_role(self, role_id: int, name: str = None) -> Optional[Role]:
        # Update a specific role by role_id
        role = db.session.query(Role).get(role_id)
        if role:
            role.name = name
            db.session.commit()
            return role

    # delete
    def delete_role(self, role_id: int) -> bool:
        # Delete a specific role by role_id
        role = db.session.query(Role).get(role_id)
        if role:
            db.session.delete(role)
            db.session.commit()
            return True
        return False

role_controller = __RoleController()
