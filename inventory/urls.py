from django.urls import path
from .views import EstablishmentListCreateAPIView, EstablishmentRetrieveUpdateDestroyAPIView, ProductListCreateAPIView, \
    ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('establishments/', EstablishmentListCreateAPIView.as_view(), name='establishment-list-create'),
    path('establishments/<int:pk>/', EstablishmentRetrieveUpdateDestroyAPIView.as_view(), name='establishment-detail'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]