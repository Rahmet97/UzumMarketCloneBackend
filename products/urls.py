from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, CategoryCreateAPIView, ProductDetailRetrieveAPIView, WishListModelViewSet, \
    BasketViewSet, ProductSearchAPIView

routers = DefaultRouter()
routers.register('product_mixins', ProductModelViewSet, '')
routers.register('wishlist_mixins', WishListModelViewSet, '')
routers.register(r'baskets', BasketViewSet)
urlpatterns = [
    path('', include(routers.urls)),
    path('category<int:pk>', CategoryCreateAPIView.as_view()),
    path('product_detail<int:pk>', ProductDetailRetrieveAPIView.as_view()),
    path('search', ProductSearchAPIView.as_view()),

]
