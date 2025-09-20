import uuid
from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    id: str = Field(max_length=36)
    name: str
    email: str
    department_id: str | None = Field(max_length=36, default=None)
    
