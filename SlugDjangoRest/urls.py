from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import routers, permissions
from api_apps.api import CategoryViewSet, ProductViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Slug Product API",
        default_version="v1",
        description="API documentation for Slug Product",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            name="Akmaral Rau",
            email="akamairau@gmail.com",
            url="https://github.com/akam18",
        ),
        license=openapi.License(
            name="BSD License",
            url= "https://ru.wikipedia.org/wiki/BSD"
        ),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
        # permissions.IsAuthenticated,
        # permissions.IsAdminUser,
    ],
)


urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),



    path('admin/', admin.site.urls),
    path('', include("main.urls")),

]



#  он должен только так писат а не то сломается , мы должны вытаскивать из settinga
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Если есть хоть один фото, мы должны сделать это
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)