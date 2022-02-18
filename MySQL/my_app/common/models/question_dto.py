from pydantic import BaseModel, EmailStr, Field


class QueryTextDto(BaseModel):
    text_content: str = Field(
        title="The text which need to be queried", max_length=10000
    )
    email: EmailStr = Field(
        title="Email", max_length=500
    )
    
class QueryDto(BaseModel):
    query: str = Field(
        title="query"
    )
    email: EmailStr = Field(
        title="Email", max_length=500
    )
   

