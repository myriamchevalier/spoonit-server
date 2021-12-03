from django.contrib.auth.models import User
from django.db import models

from spoonit_api.models import Category, Spoon, TaskList


class Task(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    spoon = models.ForeignKey(Spoon, on_delete=models.CASCADE)
    description = models.TextField()
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    is_universal = models.BooleanField()
    spoonies = models.ManyToManyField(User, through=TaskList, related_name='tasks')
