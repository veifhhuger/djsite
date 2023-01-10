from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти",]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu':menu,'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu':menu,'title': 'о сайте'})

def categories(request, catid):
    return HttpResponse(f'<h1>Страница приложения CATEGORIES<h1><p>{catid}</p>')