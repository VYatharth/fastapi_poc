from pydantic import BaseModel, Field


class Department(BaseModel):
    id: str = Field(max_length=36)
    name: str
    description: str | None = Field(max_length=500, default=None)
    
