from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserBase
from app.services import user_service

def create_user_controller(db: Session, user: UserCreate):
    return user_service.create_user(db, user)

def get_users_controller(db: Session, skip: int = 0, limit: int = 10):
    return user_service.get_users(db, skip, limit)

def get_user_controller(db: Session, user_id: int):
    return user_service.get_user_by_id(db, user_id)

def update_user_controller(db: Session, user_id: int, user_data: UserBase):
    return user_service.update_user(db, user_id, user_data)

def delete_user_controller(db: Session, user_id: int):
    return user_service.delete_user(db, user_id)
