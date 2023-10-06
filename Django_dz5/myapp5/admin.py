from django.contrib import admin
from .models import Product, Client, Order
"""
Модуль для настройки панели администрирования
"""

@admin.action(description="Очистить таблицу")
def clear_table(modeladmin, request, queryset):
    """
    Функция для работы с датасетом (пример)
    :param modeladmin:
    :param request:
    :param queryset:
    :return:
    """
    Client.all().delete()

class ClientAdmin(admin.ModelAdmin):
    """
    Класс для администрирования модели данных клиентов
    """
    list_display = ['name', 'email', 'phone', 'address', 'register_date']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name', 'email', 'address']
    search_help_text = 'Поиск по полям Name, Email, Address клиента'
    readonly_fields = ['register_date']
    actions = [clear_table]
    # fields = ['name', 'email', 'phone', 'address', 'register_date']
    fieldsets = [
        (
            'Имя клиента',
            {
                'classes': 'wide',
                'fields': ['name'],
            }
        ),
        (
            'Характеристики',
            {
                'fields': ['email', 'phone', 'address'],
            }
        ),
        (
            None,
            {
                'fields': ['register_date'],
            }
        ),
    ]

class ProductAdmin(admin.ModelAdmin):
    """
    Класс для администрирования модели данных товаров
    """
    list_display = ['name', 'price', 'amount', 'image', 'create_date']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени товара'
    readonly_fields = ['register_date']
    #fields = ['name', 'price', 'amount', 'image', 'create_date']
    readonly_fields = ['create_date']
    fieldsets = [
        (
            'Наименование товара',
            {
                'classes': 'wide',
                'fields': ['name'],
            }
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Отображение',
            {
                'fields': ['image'],
            }
        ),
        (
            None,
            {
                'fields': ['create_date'],
            }
        ),
    ]

class OrderAdmin(admin.ModelAdmin):
    """
    Класс для администрирования модели данных заказов
    """
    list_display = ['client', 'total_price', 'order_date']
    ordering = ['order_date', 'client']
    list_filter = ['order_date']
    fields = ['client', 'products', 'total_price', 'order_date']
    readonly_fields = ['order_date']


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
