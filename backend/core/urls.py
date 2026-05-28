from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('accounts.urls')),
    path('api/', include('leave_management.urls')),
    path('api/', include('complaints.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('food_menu.urls')),
    path('api/', include('dashboard.urls')),
    path('', include('dashboard.urls')),
]