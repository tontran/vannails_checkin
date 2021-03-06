from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('checkin_api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('checkin_api.urls')),
    path('tinymce/', include('tinymce.urls')),
    # path('api/auth/', include('dj_rest_auth.urls')),
    # path('api/auth/signup/', include('dj_rest_auth.registration.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)