from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path

from api.views import FullCardViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Hyperativa Sample API",
      default_version='v1',
      description="Online Documentation for Hyperativa Sample API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ricardocarmo72@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", FullCardViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    
]