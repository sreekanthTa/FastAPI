from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserBase
from app.services import user_service

async def create_user_controller(db: Session, user: UserCreate):
    return await user_service.create_user(db, user)

async def get_users_controller(db: Session, skip: int = 0, limit: int = 10):
    return await user_service.get_users(db, skip, limit)

async def get_user_controller(db: Session, user_id: int):
    return await user_service.get_user_by_id(db, user_id)

async def update_user_controller(db: Session, user_id: int, user_data: UserBase):
    return await user_service.update_user(db, user_id, user_data)

async def delete_user_controller(db: Session, user_id: int):
    return await user_service.delete_user(db, user_id)
