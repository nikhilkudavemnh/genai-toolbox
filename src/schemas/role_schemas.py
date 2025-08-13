from pydantic import BaseModel


class RoleCreateInput(BaseModel):
    name: str
    descriptions: str
    permissions: list
