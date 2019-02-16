from django.urls import path
from django.views.generic import TemplateView

from .views import ArticleAPIView, ArticleView


urlpatterns = [
    path('api/articles', ArticleAPIView.as_view()),
    path('articles', ArticleView.as_view())
]
