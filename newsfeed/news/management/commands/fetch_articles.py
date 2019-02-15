import requests

from django.core.management.base import BaseCommand, CommandError

from news.models import Article


class Command(BaseCommand):
    help = 'fetch articles from newsapi'

    def add_arguments(self, parser):
        parser.add_argument('api_key', type=str)

    def handle(self, *args, **options):
        try:
            articles = requests.get(
                'https://newsapi.org/v2/top-headlines?'
                'country=us&category=business&apiKey=' + options['api_key']
            )
            for article in articles.json()['articles']:
                Article.objects.create(
                    source_id=article['source']['id'],
                    source_name=article['source']['name'],
                    author=article['author'],
                    title=article['title'],
                    url=article['url'],
                    url_to_image=article['urlToImage'],
                    published_at=article['publishedAt'],
                    content=article['content'],
                )
        except requests.exceptions.HTTPError:
            raise CommandError('Http Error')
        except requests.exceptions.Timeout:
            raise CommandError('Request Timed Out')
