from django.shortcuts import render
from .models import News_post
# Create your views here.
def home(request):
    news = News_post.objects.select_related('user').all()  # Оптимизируем запрос
    return render(request, 'news/news.html', {'news': news})