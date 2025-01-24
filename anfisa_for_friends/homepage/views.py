# Для применения Q-объектов их нужно импортировать:
# from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    """Тестирование разных вариаций работы с моделями:
    # Запрашиваем нужные поля моделей + используем фильтр + исключаем
    # неопубликованные записи + используем Q-объекты + используется сортировка
    # по алфавиту + выводятся первые 3 объекта(через срез):
    ice_cream_list = IceCream.objects.values(
        # Запрашиваем данные модели Category, которая связана
        # с моделью IceCream:
        'id', 'title', 'description', 'category__title', 'wrapper__title'
        ).filter(Q(is_published=True) &
                 (Q(is_on_main=True) | Q(title__contains='пломбир'))
                 ).order_by('title')[:3]
    """
    # Запрашиваем нужные поля из базы данных:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
