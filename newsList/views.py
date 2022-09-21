import json
from django.shortcuts import render
import requests
from django.views.generic import View
from django.http import HttpResponse
from .models import Item




class ListNews(View):
    def get(self, *args, **kwargs):
        

        return HttpResponse()