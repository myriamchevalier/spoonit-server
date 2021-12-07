from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from spoonit_api.models import Category
from spoonit_api.serializers import CategorySerializer

class CategoryView(ViewSet):
    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()


        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
