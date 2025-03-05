# from django.urls import path
# from . import views
# from django.contrib import admin
# from django.urls import include, path
# from django.urls import path, include
# from rest_framework import routers
# from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

# # router = routers.DefaultRouter()
# # router.register(r'movies', MovieViewSet)
# # router.register(r'seats', SeatViewSet)
# # router.register(r'bookings', BookingViewSet)

# urlpatterns = [
#     path('movies/', views.movie_list, name='movie_list'),
#     path('book-seat/<int:movie_id>/', views.seat_booking, name='book_seat'),
#     path('booking-history/', views.booking_history, name='booking_history'),
#     #path('api/', include(router.urls)),
#     #path("", views.index, name="index"),
#     # Add paths for your HTML views if needed.
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views  
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

# Router for handling API endpoints listed below
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', movie_list, name='movie_list'),  # Home screen
    path('book-seat/<int:movie_id>/', seat_booking, name='seat_booking'),
    path('booking-history/', booking_history, name='booking_history'),
    path('api/', include(router.urls)),
]