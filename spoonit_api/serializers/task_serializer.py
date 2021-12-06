from rest_framework import serializers
from spoonit_api.models import Task




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'category', 'spoon', 'description', 'is_universal', 'is_active')
        depth = 1



