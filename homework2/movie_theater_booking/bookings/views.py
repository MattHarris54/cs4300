from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .models import Movie, Booking, Seat
from django.shortcuts import render, get_object_or_404, redirect

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

# Handle seat booking for specific movies
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    available_seats = Seat.objects.filter(is_booked=False)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')
        for seat_id in selected_seats:
            seat = Seat.objects.get(id=seat_id)
            if not seat.is_booked:
                seat.is_booked = True
                seat.save()
                Booking.objects.create(movie=movie, seat=seat)
        
        return redirect('/booking-history/')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'available_seats': available_seats,
    })


def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

