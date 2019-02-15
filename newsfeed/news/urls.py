from django.urls import path

from .views import ArticleView


urlpatterns = [
    path('api/articles', ArticleView.as_view()),
]
