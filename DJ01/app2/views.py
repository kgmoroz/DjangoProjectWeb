from django.http import HttpResponse

def data_page(request):
    return HttpResponse("<h1>Страница Data: Это страница с данными</h1>")

def test_page(request):
    return HttpResponse("<h1>Страница Test: Это тестовая страница</h1>")
