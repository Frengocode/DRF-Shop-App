from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from .serializers import BaseOrderSerializer
from ..models import OrderModel
from apps.cart.models import CartModel
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.db import transaction
from django.db.models import Sum
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.throttling import UserRateThrottle

import logging


log = logging.getLogger(__name__)


@extend_schema(tags=["Order"])
class CreateOrderAPIView(CreateAPIView):
    queryset = OrderModel.objects.all()
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def create(self, request, *args, **kwargs):
        carts = CartModel.objects.filter(
            user=self.request.user, is_ready_to_order=False
        )

        if carts:
            with transaction.atomic():
                order = OrderModel.objects.create(user=request.user)
                order.cart.add(*carts)

                carts.update(is_ready_to_order=True)

            return Response({"message": "Order Created Succsesfully"})
        return Response({"message": "Not yet Carts"}, status=404)


@extend_schema(tags=["Order"], responses=BaseOrderSerializer)
class GetOrdersAPIView(ListAPIView):
    queryset = OrderModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BaseOrderSerializer

    @extend_schema(responses=BaseOrderSerializer)
    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)
    
    @method_decorator(cache_page(250))
    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()

        for order in orders:
            total_price = order.cart.annotate(
                item_total=Sum("quantity") * Sum("product__price")
            ).aggregate(order_total=Sum("item_total"))["order_total"]

            order.total_price = total_price

        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
