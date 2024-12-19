from django.urls import path
from .views import CreateCartAPIView, GetCartsAPIView, RemoveCartAPIView


urlpatterns = [
    path("create-cart/<int:pk>/", CreateCartAPIView.as_view()),
    path("get-carts/", GetCartsAPIView.as_view()),
    path("delete-cart/<int:pk>/", RemoveCartAPIView.as_view()),
]
