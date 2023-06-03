from rest_framework.serializers import ModelSerializer

from apps.models import Product, ProductImage, Category


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    images = ProductImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

