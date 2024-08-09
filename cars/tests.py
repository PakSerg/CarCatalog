from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from decimal import Decimal
from .models import Car


class CarAPITests(APITestCase):

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        self.car1 = Car.objects.create(
            brand='Toyota', model='Corolla', year=2020, fuel_type='бензин',
            transmission='механическая', mileage=5000, price=20000
        )
        self.car2 = Car.objects.create(
            brand='Honda', model='Civic', year=2019, fuel_type='дизель',
            transmission='автоматическая', mileage=10000, price=22000
        )

    def test_obtain_token(self):
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_get_car_list(self):
        self.authenticate() 

        response = self.client.get('/api/cars/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_add_car(self): 
        self.authenticate() 

        car_data = {
            'brand': 'Toyota',
            'model': 'Camry',
            'year': 2023,
            'fuel_type': 'бензин',
            'transmission': 'автоматическая',
            'mileage': 0,
            'price': 30000
        }
        response = self.client.post('/api/cars/', data=car_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['brand'], car_data['brand'])
        self.assertEqual(response.data['model'], car_data['model'])
        self.assertEqual(response.data['year'], car_data['year'])
        self.assertEqual(response.data['fuel_type'], car_data['fuel_type'])
        self.assertEqual(response.data['transmission'], car_data['transmission'])
        self.assertEqual(response.data['mileage'], car_data['mileage'])
        self.assertEqual(Decimal(response.data['price']), Decimal(car_data['price']))

    def test_get_car_detail(self):
        self.authenticate() 

        response = self.client.get(f'/api/cars/{self.car1.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], self.car1.brand)
        self.assertEqual(response.data['model'], self.car1.model)
        self.assertEqual(response.data['year'], self.car1.year)
        self.assertEqual(response.data['fuel_type'], self.car1.fuel_type)
        self.assertEqual(response.data['transmission'], self.car1.transmission)
        self.assertEqual(response.data['mileage'], self.car1.mileage)
        self.assertEqual(Decimal(response.data['price']), Decimal(self.car1.price))

    def test_update_car(self):
        self.authenticate() 

        updated_data = {
            'brand': 'Toyota',
            'model': 'Camry',
            'year': 2023,
            'fuel_type': 'дизель',
            'transmission': 'автоматическая',
            'mileage': 1000,
            'price': 28000
        }
        response = self.client.put(f'/api/cars/{self.car1.id}/', data=updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], updated_data['brand'])
        self.assertEqual(response.data['model'], updated_data['model'])
        self.assertEqual(response.data['year'], updated_data['year'])
        self.assertEqual(response.data['fuel_type'], updated_data['fuel_type'])
        self.assertEqual(response.data['transmission'], updated_data['transmission'])
        self.assertEqual(response.data['mileage'], updated_data['mileage'])
        self.assertEqual(Decimal(response.data['price']), Decimal(updated_data['price']))

    def test_delete_car(self):
        self.authenticate() 

        response = self.client.delete(f'/api/cars/{self.car1.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/api/cars/{self.car1.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def authenticate(self): 
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')