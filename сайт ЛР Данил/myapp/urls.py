# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница будет использовать функцию 'index' из views.py
    path('', views.index, name='index'),
]