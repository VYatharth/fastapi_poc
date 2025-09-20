from pydantic import BaseModel, EmailStr, Field


class CreateUserDto(BaseModel):
    id: str | None = Field(title="User ID", max_length=36, default=None)
    name: str = Field(title="Name", max_length=100)
    email: EmailStr = Field(title="Email", max_length=500)
    department_id: str | None = Field(title="Department ID", max_length=36, default=None)




