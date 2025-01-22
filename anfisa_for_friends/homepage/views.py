# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Запрашиваем нужные поля моделей + используем фильтр + исключаем
    # неопубликованные записи + используем Q-объекты:
    ice_cream_list = IceCream.objects.values(
        'title', 'description'
        ).filter(Q(is_published=True) &
                 (Q(is_on_main=True) | Q(title__contains='пломбир')))
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
