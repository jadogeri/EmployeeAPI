"""
Task Model Module
-------------------
Description: SQLAlchemy database model for Task persistence.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: task_model.py
License: MIT
"""

from __future__ import annotations
from typing import List, Optional
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

# --- TASK MODEL (Many-to-One with User) ---
class TaskModel(db.Model):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))

    # Foreign Key linking to User
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="tasks")

    def __repr__(self) -> str:
        return f"<TaskModel(id={self.id}, title='{self.title}')>"