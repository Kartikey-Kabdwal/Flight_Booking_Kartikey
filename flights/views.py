from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Flight, Booking


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def search_flights(request):
    current_date = timezone.now().date()
    flights = Flight.objects.filter(departure_date__gte=current_date)
    return render(request, 'flight_list.html', {'flights': flights})

@login_required(login_url='/login/')
def cancel_flight(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking.user == request.user and booking.flight.departure_date > timezone.now().date():
        booking.flight.available_seats += 1
        booking.flight.save()
        booking.delete()
    return redirect('my_bookings')

@login_required(login_url='/login/')
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    if flight.available_seats > 0:
        Booking.objects.create(user=request.user, flight=flight)
        flight.available_seats -= 1
        flight.save()
        return redirect('my_bookings')
    return render(request, 'flight_list.html', {'message': 'No seats available'})


@login_required(login_url='/login/')
def my_bookings(request):
    current_date = timezone.now().date()
    bookings = Booking.objects.filter(user=request.user)
    for booking in bookings:
        booking.is_upcoming = booking.flight.departure_date >= current_date
    return render(request, 'my_bookings.html', {'bookings': bookings})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('search_flights')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
