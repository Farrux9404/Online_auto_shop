from django.urls import path
from .views import slider_list, slider_detail

urlpatterns = [
    path('slider/', slider_list, name='slider-list'),
    path('slider/<int:pk>/', slider_detail, name='slider-detail'),
]

