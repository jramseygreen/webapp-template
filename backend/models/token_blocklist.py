from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from backend.db import db

from datetime import datetime

class TokenBlocklist(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    jti: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    @classmethod
    def is_jti_blacklisted(cls, jti) -> bool:
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'jti': self.jti,
            'created_at': self.created_at.isoformat(),
            'expires_at': self.expires_at.isoformat()
        }
