"""
Employee Model Module
-------------------
Description: SQLAlchemy database model for Employee persistence.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-25
File: employee_model.py
License: MIT
"""
from __future__ import annotations
from infrastructure.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(40), nullable=False)
    last_name: Mapped[str] = mapped_column(String(40), nullable=False)
    email: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    role: Mapped[str] = mapped_column(String(20), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=True)


    def __repr__(self) -> str:
        return f"<UserModel {self.first_name} {self.last_name}>"

