from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, get_object_or_404
from .models import Movie, Booking, Seat
from django.shortcuts import render, get_object_or_404, redirect


# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'bookings/movie_list.html', {'movies': movies})

# def seat_booking(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     seats = Seat.objects.filter(is_booked=False)
#     if request.method == 'POST':
#         # Process booking form submission here
#         # e.g., get selected seat from POST data, create a Booking, etc.
#         pass
#     return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

# def booking_history(request):
#     # Assuming you have user authentication in place.
#     bookings = Booking.objects.filter(user=request.user)
#     return render(request, 'bookings/booking_history.html', {'bookings': bookings})
# Renders the list of movies
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



# Render the booking history for the user
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

# def base(request):
#     return render(request, 'bookings/base.html')
