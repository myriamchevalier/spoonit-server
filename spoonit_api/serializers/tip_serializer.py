from rest_framework import serializers
from .topic_serializer import TopicSerializer
from .user_serializer import UserSerializer
from spoonit_api.models import Tip

class TipSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    spoonie = UserSerializer()
    class Meta:
        model = Tip
        fields = ('id', 'topic', 'content', 'spoonie')
        depth = 1

