from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from spoonit_api.models import Spoon
from spoonit_api.serializers import SpoonSerializer

class SpoonView(ViewSet):
    def list(self, request):
        """Handle GET requests to get all spoons

        Returns:
            Response -- JSON serialized list of spoons
        """
        spoons = Spoon.objects.all()


        serializer = SpoonSerializer(spoons, many=True)
        return Response(serializer.data)
