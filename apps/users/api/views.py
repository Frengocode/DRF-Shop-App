from rest_framework.generics import (
    GenericAPIView,
    get_object_or_404,
    RetrieveAPIView,
    CreateAPIView,
)
from ..models import CustomUser
from .serializers import (
    UserSerializers,
    CreateUserSerializer,
    CreateProfilePictureSerializers,
)
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.throttling import UserRateThrottle
import logging


log = logging.getLogger(__name__)


@extend_schema(tags=["User"])
class GetUserAPIView(RetrieveAPIView):
    lookup_url_kwarg = "pk"
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return get_object_or_404(CustomUser, pk=self.kwargs.get("pk"))

    
    @extend_schema(responses=UserSerializers)
    @method_decorator(cache_page(100))
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            log.info("User not found %s", kwargs.get("pk"))
            return Response({"message": "User Not Found"}, status=404)

        serializers = self.get_serializer(queryset)
        return Response(serializers.data)


@extend_schema(tags=["User"])
class CreateUserAPIView(CreateAPIView):
    throttle_classes = [UserRateThrottle]
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


@extend_schema(
    tags=["User"],
    responses=CreateProfilePictureSerializers,
    request=CreateProfilePictureSerializers,
)
class CreateProfilePictureAPIView(CreateAPIView):
    throttle_classes = [UserRateThrottle]
    serializer_class = CreateProfilePictureSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
