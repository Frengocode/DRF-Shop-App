from django.urls import path
from .views import GetUserAPIView, CreateUserAPIView, CreateProfilePictureAPIView


urlpatterns = [
    path("get-user/<int:pk>/", GetUserAPIView.as_view()),
    path("create-user/", CreateUserAPIView.as_view()),
    path("create-profile-picture/", CreateProfilePictureAPIView.as_view()),
]
