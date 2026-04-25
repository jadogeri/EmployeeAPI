from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# You MUST pass model_class=Base here
db: SQLAlchemy = SQLAlchemy(model_class=Base)