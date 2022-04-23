#posts/views.py
from django.http import HttpResponse

#Главная страница
def index(request):
    return HttpResponse('Самая самая главная страница')

def group_posts(request, pk):
    return HttpResponse(f'Это текст из переменной pk: {pk}')