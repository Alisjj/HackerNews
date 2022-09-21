from django.shortcuts import render
from django.views import generic
from .models import Item




class ListNews(generic.ListView):
    template_name = 'newsList/home.html'
    context_object_name = "item_list"
    queryset = Item.objects.all()

