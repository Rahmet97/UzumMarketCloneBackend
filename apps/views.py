# Product
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from apps.models import Product, Category, Wishlist
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, WishListModelSerializer


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
