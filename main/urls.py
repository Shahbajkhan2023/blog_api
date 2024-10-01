from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Serve media files during development
if settings.DEBUG:  # Ensure this only runs in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)