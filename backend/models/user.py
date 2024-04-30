from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bcrypt import hashpw, checkpw, gensalt

from backend.db import db

class User(db.Model):
    serialize_rules = ('-password_hash', '-roles.users',)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=False)

    roles = relationship('Role', secondary='user_role')

    # Set and hash the user's password.
    def set_password(self, password):
        self.password_hash = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    # Check if the provided password matches the stored hashed password.
    def check_password(self, password) -> bool:
        return checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def is_admin(self) -> bool:
        for role in self.roles:
            if role.name == 'admin':
                return True
        return False
