
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
# from rest_framework_simplejwt import views as jwt_views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('users',UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('', include('users.urls')),
    path('users/login/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
