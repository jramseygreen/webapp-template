from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_serializer import SerializerMixin

class Base(DeclarativeBase, SerializerMixin):
  pass

db = SQLAlchemy(model_class=Base)
