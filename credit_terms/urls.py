from django.urls import path
from .views import creditterms_list, creditterms_detail


urlpatterns = [
    path('creditterms/', creditterms_list, name='about-list'),
    path('creditterms/<int:pk>/', creditterms_detail, name='about-detail'),
]


