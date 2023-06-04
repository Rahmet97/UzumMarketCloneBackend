# Product
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from apps.models import Product, Category, Wishlist, Order, Basket
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, WishListModelSerializer, \
    OrderModelSerializer, BasketSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


# Category
class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class WishListModelViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishListModelSerializer


class OrderCreateView(CreateAPIView):
    serializer_class = OrderModelSerializer
    queryset = Order.objects.all()


class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
