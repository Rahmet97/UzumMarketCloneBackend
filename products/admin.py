from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import Product, Category


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price')
#
#
# admin.site.register(Product, ProductAdmin)
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent')
#
#
# admin.site.register(Category, CategoryAdmin)


@admin.register(Category)
class NewAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class NewAdmin(TranslationAdmin):
    pass


