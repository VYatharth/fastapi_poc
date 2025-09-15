from pydantic import BaseModel, Field


class CreateDepartmentDto(BaseModel):
    id: str | None = Field(title="Department ID", max_length=36, default=None)
    name: str = Field(title="Name", max_length=100)
    description: str = Field(title="Description", max_length=500)


