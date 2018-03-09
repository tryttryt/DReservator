from django.contrib.auth.models import User

from .models import Users, Rooms, Reservations


def users_cp(request):
    return {'users': Users.objects.all()}


def user_cp(request):
    return {'user': User.objects.all()}


def rooms_cp(request):
    return {'rooms': Rooms.objects.all()}


def reservations_cp(request):
    return {'reservations': Reservations.objects.all()}
