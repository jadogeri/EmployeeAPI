"""
Role Model Module
-------------------
Description: SQLAlchemy database model for Role persistence.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: role_model.py
License: MIT
"""
from __future__ import annotations
from typing import List, Optional
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


# --- ROLE MODEL (One-to-One with User) ---
class RoleModel(db.Model):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)

    # Back-reference to user
    user: Mapped["UserModel"] = relationship(back_populates="role")

    def __repr__(self) -> str:
        return f"<RoleModel(id={self.id}, name='{self.name}')>"