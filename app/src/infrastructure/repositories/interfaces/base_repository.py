"""
Base Repository Module
----------------------
Description: Provides a generic base class for handling database persistence
             logic using SQLAlchemy, supporting common CRUD operations.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-APR-19
File: base_repository.py
License: MIT
"""
from __future__ import annotations
from typing import TypeVar, Generic, List, Optional, Type
from infrastructure.database import db

# Define a TypeVar to provide better type hinting for subclasses
T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    @property
    def query(self):
        """Allows self.model.query style syntax using the global db.session."""
        return db.session.query(self.model)

    def get_all(self) -> List[T]:
        return self.query.all()

    def get_one(self, entity_id: int | str) -> Optional[T]:
        return db.session.get(self.model, entity_id)

    def save(self, instance: T) -> T:
        db.session.add(instance)
        db.session.commit()
        return instance

    def delete(self, entity_id: int | str) -> bool:
        instance = self.get_one(entity_id)
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return True
        return False