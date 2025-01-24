from django.shortcuts import render, get_object_or_404

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    # Вызываем .get() и в его параметрах указываем условия фильтрации:
    ice_cream = get_object_or_404(
        IceCream.objects.filter(is_published=True,
                                category__is_published=True),
        pk=pk
        )
    context = {
        'ice_cream': ice_cream
    }
    return render(request, template, context)


"""
# Вариант только с полями title, description для оптимизации
# SQL-запроса из урока:
    ice_cream = get_object_or_404(
        IceCream.objects.values(
            'title', 'description'
            ).filter(is_published=True),
        pk=pk
        )
"""


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    # Для указания полей связанной модели в шаблоне(list.html) использована
    # точечная нотация, а это значит, что для получения связанных данных
    # для атрибута category в ORM-запросе можно воспользоваться
    # методом select_related()
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
