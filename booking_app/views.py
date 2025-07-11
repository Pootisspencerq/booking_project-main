from datetime import datetime
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import RoomForm, RegisterForm, LoginForm, BookingForm
from django import forms
from .models import Resource
from django.shortcuts import render

KONAMI_CODE = ['UP', 'UP', 'DOWN', 'DOWN', 'LEFT', 'RIGHT', 'LEFT', 'RIGHT', 'B', 'A']

def konami_view(request):
    message = ''
    if request.method == 'POST':
        code_input = request.POST.get('code', '').upper().split()
        if code_input == KONAMI_CODE:
            message = 'Вітаємо! Ви ввели Konami Code! 🎉'
        else:
            message = 'Невірний код, спробуйте ще раз.'
    return render(request, 'konami.html', {'message': message})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'booking_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'booking_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room_is_booked = Booking.objects.filter(room=room).exists()

    if request.user.is_authenticated:
        form = BookingForm(initial={'room': room})
        form.fields['room'].widget = forms.HiddenInput()
    else:
        form = None

    return render(request, 'booking_app/room_detail.html', {
        'room': room,
        'form': form,
        'room_is_booked': room_is_booked
    })


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})


@login_required
def create_booking(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room

            # Об'єднання дати + часу
            new_start = datetime.combine(booking.check_in, booking.check_in_time)
            new_end = datetime.combine(booking.check_out, booking.check_out_time)

            # Перевірка на перетин по часу
            overlapping = Booking.objects.filter(room=room).filter(
                check_in__lte=booking.check_out,
                check_out__gte=booking.check_in
            )

            for existing in overlapping:
                existing_start = datetime.combine(existing.check_in, existing.check_in_time)
                existing_end = datetime.combine(existing.check_out, existing.check_out_time)

                if new_start < existing_end and new_end > existing_start:
                    form.add_error(None, 'Ця кімната вже зайнята на вибраний час.')
                    break
            else:
                booking.save()
                return redirect('booking_success')
    else:
        form = BookingForm(initial={'room': room})
        form.fields['room'].widget = forms.HiddenInput()

    booked_dates = list(Booking.objects.filter(room=room).values_list('check_in', flat=True))
    return render(request, 'booking_form.html', {
        'form': form,
        'room': room,
        'booked_dates': booked_dates
    })
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})


def booking_success(request):
    return render(request, 'booking_success.html')
