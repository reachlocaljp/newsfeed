from django.urls import include, path

urlpatterns = [
    path('news/', include('apps.news.urls')),
]
