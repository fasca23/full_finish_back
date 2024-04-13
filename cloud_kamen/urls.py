from django.contrib import admin

# include для подключения вложенных маршрутов
from django.urls import path, include

# Для подключения статики
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Для токенов
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Для юзеров и файлов
    path('api/users/', include('cloud_api.urls.url_users')),
    path('api/files/', include('cloud_api.urls.url_files')),
]

# Для статики в дебаг режиме
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else: urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)