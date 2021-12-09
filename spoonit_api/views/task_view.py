from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from spoonit_api.models import Task, Category, Spoon
from spoonit_api.serializers.task_serializer import TaskSerializer
from rest_framework.decorators import action

class TaskView(ViewSet):
    def list(self, request):
        """Handle GET requests to get all tasks

        Returns:
            Response -- JSON serialized list of tasks
        """
        tasks = Task.objects.all()
        created_by = request.query_params.get('created_by', None)
        category = request.query_params.get('category', None)
        spoon = request.query_params.get('spoon', None)
        
        if created_by is not None:
            tasks = tasks.filter(created_by__id=request.auth.user.id)

        if spoon is not None:
            # to filter through all the tasks, must filter through the result of first query.
            tasks = tasks.filter(spoon__id=spoon)

        if category is not None:
            tasks = tasks.filter(category__id=category)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST requests to create new tasks

        Returns:
            Response -- JSON serialized task instance
        """
        # Uses the token passed in the 'Authorization' header
        created_by = self.request.user
        category = Category.objects.get(pk=request.data['categoryId'])
        spoon = Spoon.objects.get(pk=request.data['spoonId'])

        if created_by.id is not 1:
            try:
            # Create a new Python instance of the Game class
            # and set its properties from what was sent in the
            # body of the request from the client.
                task = Task.objects.create(
                    name = request.data["name"],
                    category = category,
                    spoon = spoon,
                    description = request.data["description"],
                    created_by = created_by,
                    is_universal = False,
                    is_active = True
                )
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

        else:
            try:
                task = Task.objects.create(
                    name = request.data["name"],
                    category = category,
                    spoon = spoon,
                    description = request.data["description"],
                    created_by = created_by,
                    is_universal = True,
                    is_active = True
                )
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

    @action (methods=['get'], detail=False)
    def random_task(self, request):
        
        tasks = Task.objects.all()
        created_by = request.query_params.get('created_by', None)
        category = request.query_params.get('category', None)
        spoon = request.query_params.get('spoon', None)
        
        if created_by is not None:
            tasks = tasks.filter(created_by__id=request.auth.user.id)

        if spoon is not None:
            # to filter through all the tasks, must filter through the result of first query.
            tasks = tasks.filter(spoon__id=spoon)

        if category is not None:
            tasks = tasks.filter(category__id=category)
        
        random_task = tasks.order_by('?')[0]

        serializer = TaskSerializer(random_task)
        return Response (serializer.data)

