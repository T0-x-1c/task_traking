from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_system.urls')),
    path('', include('auth_system.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
