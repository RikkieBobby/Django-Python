from django.shortcuts import render, HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(request, id):
    ls = TodoList.objects.get(id=id)
    return render(request, "main/list.html", {"ls": ls})


def home(request):
    return render(request, "main/home.html", {"name": "test"})