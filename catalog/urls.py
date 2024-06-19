from django.urls import path
from .views import *

urlpatterns = [
    path('logo/', LogoListView.as_view(), name='Logo-list'),
    path('logo/<int:pk>/', Logodetail, name='list-detail'),

    path('logo/', CarListView.as_view(), name='Car-list'),
    path('logo/<int:pk>/', Cardetail, name='Car-detail'),

    path('logo/', ContractListAPIView.as_view(), name='Contract-list'),
    path('logo/<int:pk>/', Contractdetail, name='Contract-detail'),
]