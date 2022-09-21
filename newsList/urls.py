from django.urls import path
from . import views

app_name = 'newsList'
urlpatterns = [
    path('', views.ListNews.as_view(), name="list")
]