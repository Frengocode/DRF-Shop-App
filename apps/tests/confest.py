import httpx
import pytest

BASE_URL = "http://127.0.0.1:8000/"


@pytest.mark.asyncio
async def get_token():

    data = {"username": "admin", "password": "."}

    async with httpx.AsyncClient() as cl:
        response = await cl.post(f"{BASE_URL}api/token/", json=data)
        print(response)
        return response.json().get("access")
