import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..','..'))

import pytest
from app.schemas.user_schema import UserCreate
from unittest.mock import patch, Mock, AsyncMock
from app.main import app
from app.database import get_db

# Async override
async def override_get_db():
    return Mock()

app.dependency_overrides[get_db] = override_get_db

@pytest.mark.asyncio
async def test_create_user_success():
    from app.services.user_service import create_user

    test_data = UserCreate(
        username="test username",
        email="test@gmail.com"
    )

  
    mock_db = Mock()
 
    db_mock_ref = Mock(return_value={
        "id": 1,
        "username": "test username",
        "email": "test@gmail.com"
    })
    mock_model = Mock()
    mock_model.return_value =db_mock_ref

    # ✅ Use new= to replace object
    with patch("app.services.user_service.User", new=mock_model):
        result = await create_user(mock_db, test_data)
        assert result == db_mock_ref
