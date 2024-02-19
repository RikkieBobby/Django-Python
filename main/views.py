from django.shortcuts import render, HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(request, name):
    ls = TodoList.objects.get(name=name)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
