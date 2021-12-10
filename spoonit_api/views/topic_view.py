from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from spoonit_api.models import Topic
from spoonit_api.serializers.topic_serializer import TopicSerializer

class TopicView(ViewSet):
    def list(self, request):
        """Handle GET request to get all topics
        
        Returns:
            Response -- JSON serialized list of all topics
        """
        topics = Topic.objects.all()

        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
        