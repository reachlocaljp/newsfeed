from django.db import models


class Article(models.Model):
    # some articles have no source or author, we have to allow them to be null
    source_id = models.CharField(max_length=255, null=True)
    source_name = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    url_to_image = models.URLField()
    published_at = models.DateTimeField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
