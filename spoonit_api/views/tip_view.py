from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from spoonit_api.models import Tip, Topic
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
    
    def create(self, request):
        """Handle POST requests to create new tips
        
        Returns
            Response -- JSON serialized tip instance
        """

        spoonie = request.auth.user
        topic = Topic.objects.get(pk=request.data['topicId'])

        try:
            tip = Tip.objects.create(
                topic = topic,
                content = request.data['content'],
                spoonie = spoonie
            )
            serializer = TipSerializer(tip)
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """Handle PUT requests for updating a single tip
        
        Returns:
            Response -- 204 , 404 or 500 status code
        """
        user_tip = Tip.objects.filter(spoonie__id=request.auth.user.id)
        tip = user_tip.get(pk=pk)

        try :
            tip.topic = Topic.objects.get(pk=request.data['TopicId'])
            tip.content = request.data['content']
            tip.spoonie = request.auth.user
            tip.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Tip.DoesNotExist as ex:
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single tip

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            user_tip = Tip.objects.filter(spoonie__id=request.auth.user.id)
            tip = user_tip.get(pk=pk)
            tip.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Tip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

