# Product
from django.core.cache import cache
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Category, Wishlist, Order, Basket
from products.serializers import ProductModelSerializer, CategoryModelSerializer, WishListModelSerializer, \
    OrderModelSerializer, BasketSerializer, SearchModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    # cache
    def list(self, request, *args, **kwargs):
        if cache.get('data') is None:
            cache.set('data', self.get_queryset(), timeout=60)
            return Response(self.get_serializer(self.get_queryset(), many=True).data)
        else:
            return Response(self.get_serializer(cache.get('data'), many=True).data)


class ProductDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    # view
    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = ProductModelSerializer(instance)
        return Response(serializer.data)


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


class ProductSearchAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
