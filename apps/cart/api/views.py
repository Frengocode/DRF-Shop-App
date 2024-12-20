from rest_framework.generics import GenericAPIView, get_object_or_404, ListAPIView
from ..models import CartModel
from apps.product.models import ProductModel
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BaseCartSerializer
from rest_framework.exceptions import NotFound
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.throttling import UserRateThrottle
import logging


log = logging.getLogger(__name__)


@extend_schema(tags=["Cart"])
class CreateCartAPIView(GenericAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]
    

    def post(self, request, *args, **kwargs):

        pk = kwargs.get("pk")

        if not pk:
            log.error("pk not found")
            return NotFound({"message": "Please sign in pk argument"})

        product = get_object_or_404(ProductModel, pk=pk)
        exist_cart = CartModel.objects.filter(
            user=self.request.user, product=product
        ).first()

        if exist_cart:
            exist_cart.quantity += 1
            exist_cart.save()

            return Response({"message": "Product Succsesfully added"})

        cart = CartModel(user=self.request.user, product=product)
        cart.save()
        log.info("Cart created Succsesfully %s", cart)

        return Response({"message": "Created Succsesfully"})


@extend_schema(tags=["Cart"], responses=BaseCartSerializer)
class GetCartsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BaseCartSerializer

    def get_queryset(self):
        return CartModel.objects.filter(user=self.request.user, is_ready_to_order=False)

    @method_decorator(cache_page(100))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        for cart in queryset:
            cart.total_price = cart.quantity * cart.product.price

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=["Cart"])
class RemoveCartAPIView(GenericAPIView):
    queryset = CartModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        pk = kwargs.get("pk")
        return CartModel.objects.filter(pk=pk, user=self.request.user)

    def delete(self, request, *args, **kwrags):
        queryset = self.get_queryset()
        if queryset:
            log.info("Deleted succsesfully")
            queryset.delete()

        log.info("Not Found")
        return Response({"message: Cart Not Found"}, status=404)
