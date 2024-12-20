import os.path
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    get_object_or_404,
    GenericAPIView,
    UpdateAPIView,
)
from .serializers import (
    CreateProductSerializers,
    GetProductsSerializers,
    GetProductSerializers,
    UpdateProductSerializers,
    BaseProductSerializers,
)
from ..models import ProductModel
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.exceptions import NotFound
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import os
import logging


log = logging.getLogger(__name__)


@extend_schema(tags=["Product"])
class CreateProductAPIView(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = CreateProductSerializers
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Product"])
class GetProductsAPIView(ListAPIView):
    serializer_class = GetProductsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProductModel.objects.all()

    @extend_schema(responses=GetProductsSerializers)
    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializers = self.get_serializer(queryset, many=True)
        return Response(serializers.data)


@extend_schema(tags=["Product"])
class GetProductAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetProductSerializers
    queryset = ProductModel.objects.all() 

    @extend_schema(responses=GetProductSerializers)
    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return response

    def get_object(self):
        pk = self.kwargs.get("pk")
        product = get_object_or_404(ProductModel, pk=pk)
        return product


@extend_schema(tags=["Product"])
class GetProductByCategoryAPIView(ListAPIView):
    serializer_class = GetProductsSerializers
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=GetProductsSerializers)
    def get_queryset(self):
        category = self.kwargs.get("product_category")
        products = ProductModel.objects.filter(product_category=category)
        return products
    
    
    @method_decorator(cache_page(300))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializers = self.get_serializer(queryset, many=True)
        return Response(serializers.data)

@extend_schema(tags=["Product"])
class DeleteProductAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        product = get_object_or_404(ProductModel, pk=pk)

        file_path = os.path.join(settings.MEDIA_ROOT, str(product.product_picture))
        if file_path:
            os.remove(file_path)

        if self.request.user == product.user:
            product.delete()
            log.info("deleted succsesfullt", kwargs.get("pk"))
            return Response({"message": "Deleted Succsesfully"})


@extend_schema(tags=["Product"])
class UpdateProductAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProductSerializers
    queryset = ProductModel.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        product = self.get_object()

        if product.user != request.user:
            raise NotFound({"detail": "Product not found or not authorized."})

        log.info("Product updated successfully %s", product)

        serializer = self.get_serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated successfully"})
        return Response(serializer.errors, status=400)


@extend_schema(tags=["Product"])
class SearchProductAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BaseProductSerializers

    @extend_schema(
        responses=BaseProductSerializers
    )
    @method_decorator(cache_page(100))
    def get(self, request: HttpRequest, *args, **kwargs):
        search = kwargs.get("search")
        if search is None:
            return NotFound()

        products = ProductModel.objects.filter(product_title__icontains=search)
        serializers = self.get_serializer(products, many=True)
        return Response(serializers.data)


@extend_schema(tags=["Product"])
class GetUserProductsAPIView(GenericAPIView):
    queryset = ProductModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BaseProductSerializers

    @extend_schema(responses=BaseProductSerializers)
    @method_decorator(cache_page(150))
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("user_id")
        products = ProductModel.objects.filter(user=user_id)

        serializers = self.get_serializer(products, many=True)
        return Response(serializers.data)
