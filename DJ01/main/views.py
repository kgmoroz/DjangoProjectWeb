from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'caption': 'CatDjango'})

def new(request):
    return render(request, 'main/new.html', {'caption': 'CatDjango'})

def about(request):
    return render(request, 'main/about.html', {'caption': 'CatDjango'})

def contacts(request):
    return render(request, 'main/contacts.html', {'caption': 'CatDjango'})

def blog(request):
    return render(request, 'main/blog.html', {'caption': 'Блог - CatDjango'})