from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.annotation import Annotated
from src.db.session import AsyncSession
from src.apis.deps import get_db
from src.schemas.user_schemas import UserInput
from src.db.models.user import User
from src.db.models.role import Role
from src.core.security import hash_password
user_routes = APIRouter()


@user_routes.post('/create')
async def create(user: UserInput, db:Annotated[AsyncSession,Depends(get_db)]):
    existing_user = db.query(User).filter((User.email==user.email)|(User.username==user.username)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username Or Email already exist ,Please try to login")

    hashed_password = await hash_password(user.password)
    role_id = db.query(Role).filter(Role.name==user.role).first()
    new_user = User(
        username = user.username,
        first_name = user.first_name,
        last_name = user.last_name,
        middle_name =  user.middle_name,
        email = user.email,
        dob = user.dob,
        password = hashed_password,
        is_active = True,
        role_id = role_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"username": new_user.username, "userId": new_user.id, "email": new_user.email}




