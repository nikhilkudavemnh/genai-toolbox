from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.annotation import Annotated
from src.apis.deps import get_db
from src.db.models.role import Role
from src.schemas.role_schemas import RoleCreateInput
from src.db.session import AsyncSession
user_routes = APIRouter()


@user_routes.post('/create')
async def create(role: RoleCreateInput, db:Annotated[AsyncSession,Depends(get_db)]):
    existing_role = db.query(Role).filter(Role.name==role.name).first()
    if existing_role:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role name already exists")

    new_role = Role(
        name = role.name,
        desciptions = role.description,
        permission = role.permissions
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return {"roleName": new_role.name, "roleId": new_role.id}




