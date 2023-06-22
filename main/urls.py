from django.urls import path
from .views import IndexView, ProductDetailView


urlpatterns =[
    path('', IndexView, name='index'),
    path('<slug:slug>/', ProductDetailView, name='product_detail'),
]

from rest_framework import routers, permissions
from api_apps.api import CategoryViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register('api/categories', CategoryViewSet, basename='categories')
router.register('api/products', ProductViewSet, basename='products')
urlpatterns += router.urls