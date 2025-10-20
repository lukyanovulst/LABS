from django.contrib import admin
from django.urls import path
from portfolio import views  # ← подключаем файл с нашими страницами

urlpatterns = [
    path('admin/', admin.site.urls),        # стандартная админка Django
    path('', views.home, name='home'),      # главная страница
    path('about/', views.about, name='about'),      # страница "Обо мне"
    path('skills/', views.skills, name='skills'),    # "Навыки"
    path('projects/', views.projects, name='projects'),  # "Проекты"
    path('contacts/', views.contacts, name='contacts'),  # "Контакты"
]

