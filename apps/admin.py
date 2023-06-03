from django.contrib import admin

from apps.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(Category, CategoryAdmin)
