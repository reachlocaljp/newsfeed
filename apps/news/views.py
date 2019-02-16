from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Article


class ArticleAPIView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-published_at')[:100]
        return HttpResponse('Hello World')


class ArticleView(TemplateView):
    template_name = "news/news.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        queryset = Article.objects.all().order_by('-published_at')[:20]
        context['article_list'] = queryset
        return context
