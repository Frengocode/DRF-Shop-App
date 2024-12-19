from django.urls import path
from .views import CreateOrderAPIView, GetOrdersAPIView


urlpatterns = [
    path("create-order/", CreateOrderAPIView.as_view()),
    path("get-orders/", GetOrdersAPIView.as_view()),
]
