from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    # Указываем, для каких связанных моделей нужно включить спец интерфейс:
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


# Регистрируем импортированные модели(классы), чтобы ими можно было управлять
# через админку:
# admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
# admin.site.register(IceCream)
# Регистрируем кастомное представление админ-зоны для моделей IceCream и
# Category:
admin.site.register(IceCream, IceCreamAdmin)
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'
# Регистрируем подключение вставки сортов мороженого на страницу категории:
admin.site.register(Category, CategoryAdmin)
