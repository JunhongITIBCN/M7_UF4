from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('centre/', include('centre.urls')),  
    path('admin/', admin.site.urls),
]
