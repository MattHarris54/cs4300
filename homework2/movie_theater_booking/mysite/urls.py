"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path("bookings/", include("bookings.urls")),
#     path("admin/", admin.site.urls),
# ]

# from django.urls import path
# from bookings import views
# from django.contrib import admin
# from django.urls import include, path
# from django.urls import path, include
# from rest_framework import routers
# from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

# router = routers.DefaultRouter()
# router.register(r'movies', MovieViewSet)
# router.register(r'seats', SeatViewSet)
# router.register(r'bookings', BookingViewSet)

#django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
    path('api-auth/', include('rest_framework.urls')),
    #path("", views.index, name="index"),
    #path("", views.base, name="base"),
    # Add paths for your HTML views if needed.
]
