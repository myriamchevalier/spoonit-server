from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from spoonit_api.models import Tip
from spoonit_api.serializers import TipSerializer

class TipView(ViewSet):
    def list(self, request):
        """Handles GET requests to get all tips
        
        Returns:
            Response -- JSON serialized list of tips
        """

        tips = Tip.objects.all()
        topic = request.query_params.get('topic', None)

        if topic is not None:
            tips = tips.filter(topic__id=topic)
        
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)