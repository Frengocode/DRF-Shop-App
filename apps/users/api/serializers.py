from rest_framework import serializers
from rest_framework.response import Response
from ..models import CustomUser
import logging


log = logging.getLogger(__name__)


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    profile_picture = serializers.ImageField()


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):

        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            log.error("Passwords do not match")
            raise serializers.ValidationError({"password": "Passwords do not match"})

        if CustomUser.objects.filter(username=attrs.get("username")).exists():
            log.error("Username already taken")
            raise serializers.ValidationError(
                {"username": "This username is already taken!"}
            )

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")

        user = CustomUser.objects.create(username=validated_data["username"])

        user.set_password(password)
        user.save()

        log.info("User created successfully %s", user)
        return user


class CreateProfilePictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["profile_picture"]

    def create(self, validated_data):
        user = self.context["request"].user
        user.profile_picture = validated_data.get("profile_picture")
        user.save()
        return user
