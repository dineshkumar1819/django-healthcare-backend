from django.contrib import admin  # Import the admin module to manage the admin interface
from django.urls import path, include  # Import path and include to define URL routing

urlpatterns = [
    path('admin/', admin.site.urls),  # Path for Django's default admin interface
    path('api/', include('api.urls')),  # Include URLs from the 'api' app for all API endpoints
]
