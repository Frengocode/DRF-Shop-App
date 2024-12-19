import httpx
import pytest
from apps.tests.confest import get_token, BASE_URL


@pytest.mark.asyncio
async def test_create_user():

    user_data = {
        "username": "guchi",
        "password1": "admin123321",
        "password2": "admin123321",
    }

    async with httpx.AsyncClient() as cl:
        response = await cl.post(f"{BASE_URL}user/api/v1/create-user/", json=user_data)
        assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_user():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}

    user_id = 1
    async with httpx.AsyncClient() as cl:
        response = await cl.get(
            f"{BASE_URL}user/api/v1/get-user/{user_id}/", headers=headers
        )
        assert response.status_code == 200
