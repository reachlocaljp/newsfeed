from django.db import models


class Article(models.Model):
    # some articles have no source or author, we have to allow them to be null
    source_id = models.CharField(max_length=255, null=True)
    source_name = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(unique=True)
    url_to_image = models.URLField(null=True)
    published_at = models.DateTimeField()
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_dict(self):
        # this method returns a dict in the same format as the data
        # consumed from newsapi API
        date = self.published_at.isoformat().replace('+00:00', 'Z')
        return {
            'source': {
                'id': self.source_id,
                'name': self.source_name,
            },
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'urlToImage': self.url_to_image,
            'publishedAt': date,
            'content': self.content
        }
