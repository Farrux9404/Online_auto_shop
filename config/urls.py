from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slider/', include('slider.urls')),
    path('credit_terms/', include('credit_terms.urls')),
]
