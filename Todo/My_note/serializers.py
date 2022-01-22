from .models import Tasks
from rest_framework import serializers


class Task_serilize(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields='__all__'