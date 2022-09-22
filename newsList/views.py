from django.shortcuts import render
from django.views import generic
from .models import Item
from django.db.models import Q




class ListNews(generic.ListView):
    template_name = 'newsList/home.html'
    context_object_name = "item_list"
    queryset = Item.objects.order_by('-time')
    paginate_by = 10


class NewsDetail(generic.DetailView):
    template_name= 'newsList/details.html'
    context_object_name = 'item'
    
    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset

def search(request):
    queryset = Item.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(by__icontains=query) |
            Q(text__icontains=query)
        ).distinct()
    context = {
        'item_list': queryset.order_by('-time')
    }
    return render(request, 'newsList/filter.html', context)

def filter(request, type):
    queryset = Item.objects.filter(type=type)
    context = {
        'item_list': queryset.order_by('-time')
    }
    return render(request, 'newsList/filter.html', context)
