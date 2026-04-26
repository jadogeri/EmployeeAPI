# app/domain/entities/user.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Employee:
    id: str
    first_name: str
    last_name: str
    email: str
    role: Optional[str] = None
    is_active: Optional[bool] = None

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __dict__ (self):
        return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'role': self.role, 'is_active': self.is_active}

    def __repr__ (self):
        return f'{self.first_name} {self.last_name}'
