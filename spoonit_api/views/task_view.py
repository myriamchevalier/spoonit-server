from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from spoonit_api.models import Task
from spoonit_api.serializers.task_serializer import TaskSerializer

class TaskView(ViewSet):
    def list(self, request):
        """Handle GET requests to get all tasks

        Returns:
            Response -- JSON serialized list of tasks
        """
        tasks = Task.objects.all()

        category = request.query_params.get('category', None)
        spoon = request.query_params.get('spoon', None)

        if spoon is not None:
            # to filter through all the tasks, must filter through the result of first query.
            tasks = tasks.filter(spoon__id=spoon)

        if category is not None:
            tasks = tasks.filter(category__id=category)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
