from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    spoonie = models.ForeignKey(User, on_delete=models.CASCADE)