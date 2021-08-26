from django.db import models

from crm_administration.models import SoftDelete


class Factory(SoftDelete):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
