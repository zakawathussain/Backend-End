from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Menu, Booking

class MenuTests(APITestCase):
    def test_create_menu(self):
        url = reverse('menu-list')
        data = {'name': 'Pizza', 'price': '10.99', 'description': 'Cheese Pizza'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class BookingTests(APITestCase):
    def test_create_booking(self):
        url = reverse('booking-list')
        data = {'name': 'John', 'no_of_guests': 4, 'booking_date': '2023-10-01T12:00:00Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)