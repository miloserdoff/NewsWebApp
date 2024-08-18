from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def news_home(request):
    news = Article.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')


    form = ArticleForm()
    data = {
        'form': form,
    }
    return render(request, 'news/create.html', data)