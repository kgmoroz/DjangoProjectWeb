from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    news = News_post.objects.select_related('user').all()  # Оптимизируем запрос
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ""
    if request.method == "POST":
        form = News_postForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)

            # Преобразуем строку в datetime
            pub_date_str = request.POST.get("pub_date")
            if pub_date_str:
                news.pub_date = datetime.strptime(pub_date_str, "%Y-%m-%dT%H:%M")

            # Назначаем "по умолчанию" админа, если пользователь не залогинен
            admin_user = User.objects.filter(is_superuser=True).first()
            news.user = admin_user if admin_user else None

            news.save()
            return redirect("news_home")
        else:
            error = "Данные были заполнены некорректно"
    else:
        form = News_postForm()

    return render(request, "news/add_new_post.html", {"form": form, "errors": error})