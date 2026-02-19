import pytest
from httpx import AsyncClient
from ..main import app


@pytest.mark.asyncio
async def test_register_and_login(monkeypatch):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # register
        payload = {"email": "test@example.com", "password": "secret"}
        r = await ac.post("/auth/register", json=payload)
        assert r.status_code == 200
        data = r.json()
        assert data["email"] == "test@example.com"

        # login
        r2 = await ac.post("/auth/token", json=payload)
        assert r2.status_code == 200
        token_data = r2.json()
        assert "access_token" in token_data
