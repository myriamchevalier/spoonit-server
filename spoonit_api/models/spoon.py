from django.db import models

class Spoon(models.Model):
    number_of_spoons = models.IntegerField()