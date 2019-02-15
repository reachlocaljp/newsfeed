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
            print(articles.json()['articles'])
        except requests.exceptions.HTTPError:
            raise CommandError('Http Error')
        except requests.exceptions.Timeout:
            raise CommandError('Request Timed Out')
