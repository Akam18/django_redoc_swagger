from rest_framework import routers, permissions
from api_apps.api import CategoryViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register('api.categories', CategoryViewSet, basename='categories')
router.register('api.products', ProductViewSet, basename='products')

