from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

