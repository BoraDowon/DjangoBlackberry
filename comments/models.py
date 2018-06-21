from django.db import models
from treebeard.mp_tree import MP_Node

from articles.models import Article


class Comment(MP_Node):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    contents = models.CharField(null=False, max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
