"""
User Model Module
-------------------
Description: SQLAlchemy database model for User persistence.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: user_model.py
License: MIT
"""
from __future__ import annotations
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class UserModel(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(40), nullable=False)
    last_name: Mapped[str] = mapped_column(String(40), nullable=False)
    email: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)

   # 1. ONE-TO-ONE: User has one Role
    role_id: Mapped[Optional[int]] = mapped_column(ForeignKey("roles.id"))
    role: Mapped[Optional["RoleModel"]] = relationship(back_populates="user")

    # 2. ONE-TO-MANY: User has many Tasks
    tasks: Mapped[List["TaskModel"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<UserModel {self.first_name} {self.last_name}>"

