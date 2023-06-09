# Product
from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Category, Wishlist, Order, Basket, Comment, Rating
from products.serializers import ProductModelSerializer, CategoryModelSerializer, WishListModelSerializer, \
    OrderModelSerializer, BasketSerializer, SearchModelSerializer, CommentModelSerializer, RatingModelSerializer


#  Product
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = PageNumberPagination

    # discount
    @action(detail=True, methods=['POST'])
    def add_discount(self, request, pk=None):
        product = self.get_object()
        discount = request.data.get('discount')

        product.price -= discount
        product.save()

        serializer = self.get_serializer(product)
        return Response(serializer.data)

    # cache
    def list(self, request, *args, **kwargs):
        if cache.get('data') is None:
            cache.set('data', self.get_queryset(), timeout=60)
            return Response(self.get_serializer(self.get_queryset(), many=True).data)
        else:
            return Response(self.get_serializer(cache.get('data'), many=True).data)


#  ProductDetail
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


# WishList
class WishListModelViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishListModelSerializer


# Order
class OrderCreateView(CreateAPIView):
    serializer_class = OrderModelSerializer
    queryset = Order.objects.all()


#  Basket
class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


#  Search
class ProductSearchAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer


class RatingCreateView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
