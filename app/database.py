from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#   POSTGRES_USER: postgres_user
#       POSTGRES_PASSWORD: postgres_password 
#       POSTGRES_DB: postgres_db

DATABASE_URL = "postgresql+psycopg2://postgres_user:postgres_password@localhost:5432/postgres_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()