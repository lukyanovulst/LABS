# myapp/views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Данил | Full-Stack Разработчик на Django', # Обновленный заголовок
        'content': 'Я специализируюсь на создании быстрых, безопасных и масштабируемых веб-приложений.', # Обновленный контент
    }
    return render(request, 'index.html', context)