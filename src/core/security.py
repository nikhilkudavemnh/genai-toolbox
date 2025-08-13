from passlib.context import CryptContext
from sqlalchemy.util import deprecated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def hash_password(password:str):
    return pwd_context.hash(password)


async def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)


