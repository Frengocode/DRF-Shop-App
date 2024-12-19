from apps.tests.confest import get_token
import httpx
import pytest

BASE_URL = "http://127.0.0.1:8000/order/api/v1"


@pytest.mark.asyncio
async def test_create_order():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.post(f"{BASE_URL}/create-order/", headers=headers)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_orders():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as cl:
        response = await cl.get(f"{BASE_URL}/get-orders/", headers=headers)
        assert response.status_code == 200
