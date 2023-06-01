from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    merchant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='merchant')
    price = models.FloatField()
    discount_percentage = models.FloatField()
    color = models.CharField(max_length=100)
    delivery_period = models.CharField(max_length=50)
    delivery_price = models.FloatField()
    quantity = models.IntegerField()
    short_description = models.TextField()
    description = models.TextField()
    instructions = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.image.name
