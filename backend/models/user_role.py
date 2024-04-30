from sqlalchemy import Integer, String, ForeignKey, inspect
from sqlalchemy.orm import Mapped, mapped_column
from backend.db import db

class UserRole(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id', ondelete='CASCADE'), nullable=False)
