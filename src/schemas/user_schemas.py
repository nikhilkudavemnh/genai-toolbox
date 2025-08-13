from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    email: str
    first_name: str
    middle_name: str
    last_name: str
    dob: str
    is_active: bool
    password: str
    role_name: str
