from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import Product, Category, Comment


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price')
#
#
# admin.site.register(Product, ProductAdmin)
#
#
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Comment, CommentAdmin)


@admin.register(Category)
class NewAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class NewAdmin(TranslationAdmin):
    pass


