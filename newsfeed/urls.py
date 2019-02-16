from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('news/', include('apps.news.urls')),
    path('admin/', admin.site.urls),
]
