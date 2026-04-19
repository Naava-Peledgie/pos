from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.admin_site.urls),
    path('', include('core.urls')), # This connects your core app
]