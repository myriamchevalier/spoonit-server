from rest_framework import serializers
from .user_serializer import UserSerializer
from spoonit_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Task
        fields = ('id', 'name', 'category', 'spoon', 'description', 'is_universal', 'is_active', 'created_by')
        depth = 1
