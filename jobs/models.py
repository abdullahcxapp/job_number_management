from django.db import models


class JobNumber(models.Model):
    number = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
