from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, TextField, ForeignKey, CASCADE, ImageField, DateTimeField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=150)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField(upload_to='products/images/')
    products = ForeignKey('Product', CASCADE)

    def __str__(self):
        return self.products.title


class Product(Model):
    title = CharField(max_length=150)
    price = IntegerField()
    description = TextField(blank=True, null=True)
    discount = IntegerField(null=True, blank=True)
    quantity = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    views = IntegerField(default=0)
    category = ForeignKey('Category', CASCADE)
    owner = ForeignKey('auth.User', CASCADE)

    def __str__(self):
        return self.title
