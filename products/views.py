# Product
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Category, Wishlist, Order, Basket, Comment, Rating, ViewedProduct
from products.serializers import ProductModelSerializer, CategoryModelSerializer, WishListModelSerializer, \
    OrderModelSerializer, BasketSerializer, SearchModelSerializer, CommentModelSerializer, RatingModelSerializer, \
    ViewedProductSerializer


#  Product
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = PageNumberPagination

    # Popular product
    @action(detail=True, methods=['GET'])
    def popular_product(self, request, pk=None):
        popular_products = Product.objects.order_by('-popularity_score')[:10]  # Get top 10 products by popularity score
        serializer = ProductModelSerializer(popular_products, many=True)
        return Response(serializer.data)

    # Similar products
    @action(detail=True, methods=['GET'])
    def similar_products(self, request, pk=None):
        product = self.get_object()
        similar_products = Product.objects.filter(category=product.category)[:5]
        serializer = ProductModelSerializer(similar_products, many=True)
        return Response(serializer.data)

    # Products viewed
    @action(detail=True, methods=['POST'])
    def mark_viewed(self, request, pk=None):
        product = self.get_object()

        user = request.user

        viewed_product = ViewedProduct(user=user, product=product)
        viewed_product.save()

        serializer = ViewedProductSerializer(viewed_product)
        return Response(serializer.data)

    # discount
    @action(detail=True, methods=['POST'])
    def add_discount(self, request, pk=None):
        product = self.get_object()
        discount = request.data.get('discount')

        product.price -= discount
        product.save()

        serializer = self.get_serializer(product)
        return Response(serializer.data)

    # discount products

    @action(detail=True, methods=['post'])
    def discount(self, request, pk=None):
        product = self.get_object()
        discount_percentage = request.data.get('discount_percentage')
        if discount_percentage is not None:
            product.price -= (product.price * (discount_percentage / 100))
            product.save()
            return Response({'message': 'Discount applied successfully.'})
        else:
            return Response({'error': 'Please provide a valid discount percentage.'},
                            status=status.HTTP_400_BAD_REQUEST)

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
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['option__color', 'price']

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
