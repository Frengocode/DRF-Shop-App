from apps.tests.confest import get_token, BASE_URL
import pytest
import httpx

BASE_URL = "http://127.0.0.1:8000/cart/api/v1"


@pytest.mark.asyncio
async def test_create_cart():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as cl:
        response = await cl.post(f"{BASE_URL}/create-cart/{9}/", headers=headers)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_carts():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as cl:
        response = await cl.get(f"{BASE_URL}/get-carts/", headers=headers)
        assert response.status_code == 200
