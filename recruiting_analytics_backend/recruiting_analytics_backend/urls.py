from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/obtain_token', obtain_jwt_token),
    path('management/', include('cohort_management.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)