import requests

from django.core.management.base import BaseCommand, CommandError

from apps.news.models import Article


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
        except requests.exceptions.HTTPError:
            raise CommandError('Http Error')
        except requests.exceptions.Timeout:
            raise CommandError('Request Timed Out')
        for article in articles.json()['articles']:
            # I would usually use serializers from Django rest framework
            # to validate data fetched from external sources
            try:
                Article.objects.create(
                    source_id=article['source']['id'],
                    source_name=article['source']['name'],
                    author=article['author'],
                    title=article['title'],
                    description=article['description'],
                    url=article['url'],
                    url_to_image=article['urlToImage'],
                    published_at=article['publishedAt'],
                    content=article['content'],
                )
            except (KeyError, ValueError):
                print('could not save article in the database')
