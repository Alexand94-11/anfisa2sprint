# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Запрашиваем нужные поля моделей + используем фильтр + исключаем
    # неопубликованные записи + используем Q-объекты + используется сортировка
    # по алфавиту + выводятся первые 3 объекта(через срез):
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        ).filter(Q(is_published=True) &
                 (Q(is_on_main=True) | Q(title__contains='пломбир'))
                 ).order_by('title')[:3]
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
