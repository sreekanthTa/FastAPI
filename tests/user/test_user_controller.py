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
    from app.controllers.user_controller import create_user_controller

    test_data = UserCreate(
        username="test username",
        email="test@gmail.com"
    )

    mock_service = Mock()
    mock_service.create_user = AsyncMock(return_value={
        "id": 1,
        "username": "test username",
        "email": "test@gmail.com"
    })

    mock_db = Mock()

    # ✅ Use new= to replace object
    with patch("app.controllers.user_controller.user_service", new=mock_service):
        result = await create_user_controller(test_data, mock_db)
        assert result["id"] == 1
