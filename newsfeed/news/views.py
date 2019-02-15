from django.http import HttpResponse
from django.views import View

from .models import Article


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-published_at')[:100]
        return HttpResponse('Hello World')
