from django.contrib import admin
from django.urls import path, include
from newsList.views import ListNews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListNews.as_view(), name="home"),
    path('news/', include('newsList.urls', namespace="news")),
]
