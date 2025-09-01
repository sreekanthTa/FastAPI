from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserBase

def create_user(db: Session, user: UserCreate):
    return {
     "username": "test",
    "email": "EmailStr",
    "full_name": "str" 
    }
    db_user = User(username=user.username, email=user.email, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
     return [{
    "id":1,
     "username": "test",
    "email": "EmailStr@gmail.com",
    "full_name": "str" 
    }]

    # return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user_data: UserBase):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db_user.username = user_data.username
    db_user.email = user_data.email
    db_user.full_name = user_data.full_name
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
