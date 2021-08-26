from django.db import models


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        if self.is_active is not True: return
        self.is_active = False
        self.save()

    class Meta:
        abstract = True