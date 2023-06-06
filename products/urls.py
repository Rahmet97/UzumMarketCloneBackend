from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, CategoryCreateAPIView, ProductDetailRetrieveAPIView, WishListModelViewSet, \
    BasketViewSet, ProductSearchAPIView, CommentViewSet

routers = DefaultRouter()

routers.register('product_mixins', ProductModelViewSet, 'product_mixins')
routers.register('wishlist_mixins', WishListModelViewSet, 'wishlist_mixins')
routers.register('baskets', BasketViewSet, 'baskets')
routers.register('comment', CommentViewSet, 'comments')

urlpatterns = [

    path('category/<int:pk>', CategoryCreateAPIView.as_view()),
    path('product_detail/<int:pk>', ProductDetailRetrieveAPIView.as_view()),
    path('search/', ProductSearchAPIView.as_view()),
    path('', include(routers.urls)),
]
