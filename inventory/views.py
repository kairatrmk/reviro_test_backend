from rest_framework import generics
from .models import Establishment, Product
from .serializers import EstablishmentSerializer, ProductSerializer


class EstablishmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related("establishment")
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related("establishment")
    serializer_class = ProductSerializer
