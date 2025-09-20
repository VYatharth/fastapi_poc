from fastapi import HTTPException
import traceback

class UserNotFoundException(HTTPException):
    def __init__(self, user_id=None):
        message = f"User with id {user_id} not found"
        super().__init__(status_code=404, detail=message)


class UserUpdateException(HTTPException):
    def __init__(self, user):
        traceback.print_exc()
        message = f"Error in updating user {user}"
        super().__init__(status_code=500, detail=message)
        
class DepartmentNotFoundException(HTTPException):
    def __init__(self, department_id=None):
        message = f"Department with id {department_id} not found"
        super().__init__(status_code=404, detail=message)


class DepartmentUpdateException(HTTPException):
    def __init__(self, department):
        traceback.print_exc()
        message = f"Error in updating Department {department}"
        super().__init__(status_code=500, detail=message)
