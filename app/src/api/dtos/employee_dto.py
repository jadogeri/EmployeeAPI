from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# --- BASE: Fields shared by almost everyone ---
class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=40)
    last_name: str = Field(..., min_length=2, max_length=40)
    email: EmailStr

# --- CREATE: Used for POST (Fields are mandatory) ---
class EmployeeCreate(EmployeeBase):
    password: str = Field(..., min_length=8)


# --- UPDATE: Used for PATCH (All fields are optional) ---
class EmployeeUpdate(BaseModel):
    # We don't inherit from EmployeeBase here because everything must be Optional
    # so the Employee can update just ONE field if they want.
    first_name: Optional[str] = Field(None, min_length=2)
    last_name: Optional[str] = Field(None, min_length=2)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)


# --- READ: Used for Responses (Includes ID) ---
class EmployeeRead(EmployeeBase):
    id: str

    class Config:
        from_attributes = True
