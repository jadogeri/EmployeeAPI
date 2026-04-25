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
from extensions import db

# Define a TypeVar to provide better type hinting for subclasses
T = TypeVar('T')


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        """
        Initializes the repository with a specific SQLAlchemy model.

        Args:
            model (Type[T]): The SQLAlchemy model class to manage.
        """
        self.model = model

    def get_all(self) -> List[T]:
        """
        Retrieves all records for the associated model.

        Returns:
            List[T]: A list of all entity instances.
        """
        return self.model.query.all()

    def get_one(self, entity_id: int | str) -> Optional[T]:
        """
        Retrieves a single record by its primary key.

        Args:
            entity_id (int | str): The ID of the entity to fetch.

        Returns:
            Optional[T]: The entity instance if found, otherwise None.
        """
        return self.model.query.get(entity_id)

    def save(self, instance: T) -> T:
        """
        Persists a new or updated entity instance to the database.

        Args:
            instance (T): The entity instance to save.

        Returns:
            T: The persisted entity instance.
        """
        db.session.add(instance)
        db.session.commit()
        return instance

    def delete(self, entity_id: int | str) -> bool:
        """
        Removes an entity from the database by its ID.

        Args:
            entity_id (int | str): The ID of the entity to delete.

        Returns:
            bool: True if the deletion was successful, False if entity not found.
        """
        instance = self.get_one(entity_id)
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return True
        return False