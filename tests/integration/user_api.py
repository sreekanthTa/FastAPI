
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..','..'))
from sqlmodel import select

from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool  
import pytest
from app.main import app
from app.database import get_db
from app.models.user_model import Base
from app.models.user_model import User


@pytest.fixture(name="session")  
def session_fixture():  
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session  
 

@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session

    app.dependency_overrides[get_db] = get_session_override  

    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()  


@pytest.mark.asyncio
async def test_user_creation(client, session):
    response = client.post("/users", json={
        "username":"test_username",
        "email":"test@gmail.com",
    })

    print("response is", response.json())
    statement = select(User).where(User.username == "test_username")
    result = session.exec(statement).first()  # returns the first matching User or None

    print("result",result.id)



