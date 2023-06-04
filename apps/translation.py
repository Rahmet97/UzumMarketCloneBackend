from modeltranslation.translator import register, TranslationOptions

from apps.models import Category, Product


@register(Category)
class NewTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Product)
class NewTranslationOption(TranslationOptions):
    fields = ('title', 'description')

