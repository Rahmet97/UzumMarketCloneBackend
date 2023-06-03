from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, CategoryCreateAPIView, ProductDetailRetrieveAPIView, WishListModelViewSet

routers = DefaultRouter()
routers.register('product_mixins/', ProductModelViewSet, '')
routers.register('wishlist_mixins/', WishListModelViewSet, '')
urlpatterns = [
    path('', include(routers.urls)),
    path('category/<int:pk>', CategoryCreateAPIView.as_view()),
    path('product_detail/<int:pk>', ProductDetailRetrieveAPIView.as_view()),

]
