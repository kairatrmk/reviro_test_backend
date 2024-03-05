from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Establishment, Product
from .serializers import EstablishmentSerializer, ProductSerializer


class EstablishmentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.establishment1 = Establishment.objects.create(name='Establishment 1', description='Description 1',
                                                           locations='Location 1', opening_hours='9 AM - 5 PM')
        self.establishment2 = Establishment.objects.create(name='Establishment 2', description='Description 2',
                                                           locations='Location 2', opening_hours='10 AM - 6 PM')

    def test_list_establishments(self):
        response = self.client.get(reverse('establishment-list-create'))
        establishments = Establishment.objects.all()
        serializer = EstablishmentSerializer(establishments, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_establishment(self):
        response = self.client.get(reverse('establishment-detail', kwargs={'pk': self.establishment1.pk}))
        establishment = Establishment.objects.get(pk=self.establishment1.pk)
        serializer = EstablishmentSerializer(establishment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_establishment(self):
        data = {'name': 'New Establishment', 'description': 'New Description', 'locations': 'New Location',
                'opening_hours': '9 AM - 5 PM'}
        response = self.client.post(reverse('establishment-list-create'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Establishment.objects.filter(name='New Establishment').exists())

    def test_update_establishment(self):
        data = {'name': 'Updated Establishment', 'description': 'Updated Description', 'locations': 'Updated Location',
                'opening_hours': '10 AM - 6 PM'}
        response = self.client.put(reverse('establishment-detail', kwargs={'pk': self.establishment1.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Establishment.objects.get(pk=self.establishment1.pk).name, 'Updated Establishment')

    def test_delete_establishment(self):
        response = self.client.delete(reverse('establishment-detail', kwargs={'pk': self.establishment1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Establishment.objects.filter(pk=self.establishment1.pk).exists())


class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.establishment1 = Establishment.objects.create(name='Establishment 1', description='Description 1',
                                                            locations='Location 1', opening_hours='9 AM - 5 PM')
        self.product1 = Product.objects.create(name='Product 1', description='Description 1', price=10.0,
                                                quantity=100, establishment=self.establishment1)
        self.product2 = Product.objects.create(name='Product 2', description='Description 2', price=15.0,
                                                quantity=50, establishment=self.establishment1)

    def test_list_products(self):
        response = self.client.get(reverse('product-list-create'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        response = self.client.get(reverse('product-detail', kwargs={'pk': self.product1.pk}))
        product = Product.objects.get(pk=self.product1.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.0, 'quantity': 50,
                'establishment': self.establishment1.pk}
        response = self.client.post(reverse('product-list-create'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Product.objects.filter(name='New Product').exists())

    def test_update_product(self):
        data = {'name': 'Updated Product', 'description': 'Updated Description', 'price': 25.0, 'quantity': 75,
                'establishment': self.establishment1.pk}
        response = self.client.put(reverse('product-detail', kwargs={'pk': self.product1.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(pk=self.product1.pk).name, 'Updated Product')

    def test_delete_product(self):
        response = self.client.delete(reverse('product-detail', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product1.pk).exists())