from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, CategoryCreateAPIView, ProductDetailRetrieveAPIView

routers = DefaultRouter()
routers.register('product_mixins/', ProductModelViewSet, '')

urlpatterns = [
    path('', include(routers.urls)),
    path('category/<int:pk>', CategoryCreateAPIView.as_view()),
    path('product_detail/<int:pk>', ProductDetailRetrieveAPIView.as_view()),

]
