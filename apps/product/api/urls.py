from django.urls import path
from .views import (
    CreateProductAPIView,
    GetProductsAPIView,
    GetProductAPIView,
    GetProductByCategoryAPIView,
    DeleteProductAPIView,
    UpdateProductAPIView,
    SearchProductAPIView,
    GetUserProductsAPIView,
)


urlpatterns = [
    path("create-product/", CreateProductAPIView.as_view()),
    path("get-products/", GetProductsAPIView.as_view()),
    path("get-product/<int:pk>/", GetProductAPIView.as_view()),
    path(
        "get-product-by-category/<str:product_category>/",
        GetProductByCategoryAPIView.as_view(),
    ),
    path("delete-product/<int:pk>/", DeleteProductAPIView.as_view()),
    path("update-product/<int:pk>/", UpdateProductAPIView.as_view()),
    path("search-product/<str:search>/", SearchProductAPIView.as_view()),
    path("get-user-products/<int:user_id>/", GetUserProductsAPIView.as_view()),
]
