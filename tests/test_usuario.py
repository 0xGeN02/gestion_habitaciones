"""
Tests for the Usuario API
"""

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from app.main import app

@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.fixture
async def async_client():
    async with AsyncClient(base_url="http://test") as ac:
        yield ac
