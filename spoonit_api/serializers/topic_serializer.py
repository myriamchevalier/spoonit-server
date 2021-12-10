from rest_framework import serializers
from spoonit_api.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'label')
        depth = 1

