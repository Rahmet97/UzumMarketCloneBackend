from rest_framework.serializers import ModelSerializer

from products.models import Product, ProductImage, Category, Wishlist, Order, Basket


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


class WishListModelSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ('id',)


class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class SearchModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description')
