from django.urls import path
from . import views

urlpatterns = [
    path('news-list/', views.ItemListView.as_view(), name="news-api"),
    path('comment-list/', views.CommentList.as_view(), name="comment-api"),
    path('create/', views.NewsCreateView.as_view(), name="create-api"),
    path('update/<str:pk>/', views.ItemUpdate.as_view(), name="update-news"),
    path('delete/<str:pk>/', views.ItemDestroy.as_view(), name="update-news"),
]