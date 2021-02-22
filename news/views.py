from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Categories
from .forms import NewsForm

def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})


def get_category(request, category_id):
    news = News.objects.filter(category__pk = category_id)
    current_category = Categories.objects.get(pk = category_id)
    return render(request, 'news/category.html', {'news': news, 'current_category': current_category})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    if news_item:
        return render(request, 'news/view_news.html', {'news_item': news_item})

def add_news(request):
    if request.method == 'POST':
        pass
    else: 
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})