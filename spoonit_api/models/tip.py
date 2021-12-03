from django.db import models

from django.contrib.auth.models import User

class Tip(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    content = models.TextField()
    spoonie = models.ForeignKey(User, on_delete=models.CASCADE)