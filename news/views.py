from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Categories
from .forms import NewsForm
from django.urls import reverse_lazy
from django.views.generic import ListView

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published = True)
    

# def index(request):
#     news = News.objects.all()
#     return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})


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
        form = NewsForm(request.POST)
        if form.is_valid():
            # для несвязаной формы с моделями news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news.get_absolute_url())
    else: 
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})