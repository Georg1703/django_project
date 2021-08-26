from django.db import models
from factories.models import Factory


class Deposit(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    factory = models.ForeignKey(Factory, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
