from django.shortcuts import render
from django.views import generic
from .models import Item




class ListNews(generic.ListView):
    template_name = 'newsList/home.html'
    context_object_name = "item_list"
    queryset = Item.objects.order_by('-time')


class NewsDetail(generic.DetailView):
    template_name= 'newsList/details.html'
    context_object_name = 'item'
    
    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset
