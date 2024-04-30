from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import db
from .user_role import UserRole  # Adjust the import path as needed

class Role(db.Model):
    serialize_rules = ('-users.roles',)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    users = relationship('User', secondary='user_role', overlaps="roles")
