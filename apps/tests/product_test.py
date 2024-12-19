from apps.tests.confest import get_token, BASE_URL
from pathlib import Path
import httpx
import pytest


@pytest.mark.asyncio
async def test_create_product():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}

    current_dir = Path(__file__).parent
    picture_path = current_dir / "test.jpg"

    files = {"product_picture": picture_path.open("rb")}

    data = {
        "product_title": "Test product",
        "price": 100,
        "description": "test Product description",
        "product_category": "Техника",
    }

    async with httpx.AsyncClient() as cl:
        response = await cl.post(
            f"{BASE_URL}product/api/v1/create-product/",
            files=files,
            data=data,
            headers=headers,
        )
        assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_get_product_by_category():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}
    category = "Техника"
    async with httpx.AsyncClient() as cl:
        response = await cl.get(
            f"{BASE_URL}product/api/v1/get-product-by-category/{category}/",
            headers=headers,
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_product():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.get(
            f"{BASE_URL}product/api/v1/get-product/{7}/", headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_product():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.delete(
            f"{BASE_URL}product/api/v1/delete-product/{8}/", headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_products():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.get(
            f"{BASE_URL}product/api/v1/get-products/", headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_search_product():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}
    search = "M"
    async with httpx.AsyncClient() as cl:
        response = await cl.get(
            f"{BASE_URL}product/api/v1/search-product/{search}/", headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_product():
    token = await get_token()
    headers = {"Authorization": f"Bearer {token}"}

    current_dir = Path(__file__).parent
    picture_path = current_dir / "test.jpg"

    files = {"product_picture": picture_path.open("rb")}

    data = {
        "product_title": "Test product",
        "price": 100,
        "description": "test Product description",
        "product_category": "Техника",
    }

    async with httpx.AsyncClient() as cl:
        response = await cl.patch(
            f"{BASE_URL}product/api/v1/update-product/{6}/",
            files=files,
            data=data,
            headers=headers,
        )
        assert response.status_code == 200
