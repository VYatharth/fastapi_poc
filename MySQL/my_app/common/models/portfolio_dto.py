from typing import Annotated, Any
from pydantic import BaseModel, ValidationError, WrapValidator
from pydantic_core import PydanticUseDefault

def default_on_error(v, handler) -> Any:
    """
    Raise a PydanticUseDefault exception if the value is missing.

    This is useful for avoiding errors from partial
    JSON preventing successful validation.
    """
    try:
        return handler(v)
    except ValidationError as exc:
        # there might be other types of errors resulting from partial JSON parsing
        # that you allow here, feel free to customize as needed
        if all(e['type'] == 'missing' for e in exc.errors()):
            raise PydanticUseDefault()
        else:
            raise


class PortfolioDto(BaseModel):
    personal_details: Annotated[ Any | None, WrapValidator(default_on_error) ] = None
    skills: Annotated[ Any | None, WrapValidator(default_on_error) ] = None
    achievements: Annotated[ Any | None, WrapValidator(default_on_error) ] = None
    experience: Annotated[ Any | None, WrapValidator(default_on_error) ] = None
    activities: Annotated[ Any | None, WrapValidator(default_on_error) ] = None
    contact_info: Annotated[ Any | None, WrapValidator(default_on_error) ] = None
    


