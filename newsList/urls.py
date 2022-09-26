from django.urls import path
from . import views

app_name = 'newsList'
urlpatterns = [
    path('search/', views.search, name="search"),
    path('<str:pk>/', views.NewsDetail.as_view(), name="news_details"),
    path('filter/<str:type>', views.filter, name="filter"),
]