from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path, include

from api.views import FullCardViewSet

router = routers.DefaultRouter()
router.register(r'api', FullCardViewSet, basename="api")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]