from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuList.as_view(), name='menu-list'),
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
    path('registration/', views.CustomAuthToken.as_view(), name='registration'),
]