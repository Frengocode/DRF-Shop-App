from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".envs/.env")


class AppConfig(serializers.Serializer):
    PG_USERNAME = serializers.CharField()
    PG_PASSWORD = serializers.CharField()
    PG_HOST = serializers.CharField()
    PG_PORT = serializers.IntegerField()
    DB_NAME = serializers.CharField()


raw_config = {
    "PG_USERNAME": os.getenv("PG_USERNAME"),
    "PG_PASSWORD": os.getenv("PG_PASSWORD"),
    "PG_HOST": os.getenv("PG_HOST"),
    "PG_PORT": os.getenv("PG_PORT"),
    "DB_NAME": os.getenv("DB_NAME"),
    "REDIS_CLI": os.getenv("REDIS_CLI"),
}


serializer = AppConfig(data=raw_config)
if not serializer.is_valid():
    raise ValidationError(serializer.errors)


validated_config = serializer.validated_data
