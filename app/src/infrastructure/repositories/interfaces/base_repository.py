from __future__ import annotations
from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.orm import Session  # Import standard Session

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    @property
    def query(self):
        """Uses the injected session instead of Flask's global context."""
        return self.session.query(self.model)

    def get_all(self) -> List[T]:
        return self.query.all()

    def get_one(self, entity_id: int | str) -> Optional[T]:
        return self.session.get(self.model, entity_id)

    def save(self, instance: T) -> T:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, entity_id: int | str) -> bool:
        instance = self.get_one(entity_id)
        if instance:
            self.session.delete(instance)
            self.session.commit()
            return True
        return False
