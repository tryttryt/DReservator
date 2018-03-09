from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


ACTIVITIES = (
    ("Lekcja", "Lekcja"),
    ("Ćwiczenia", "Ćwiczenia")
)


class UsersAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "address", "phone", "is_instructor", "first_time")


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nazwa użytkownika")
    address = models.CharField(max_length=255, blank=True, verbose_name="Adres",
                               help_text="np. ul.Krajobrazowa 8/1, 00-001, Twoje Miasto")
    phone = models.CharField(max_length=12, blank=True, verbose_name="Telefon", help_text="+48 123 123 123")
    is_instructor = models.BooleanField(default=False, verbose_name="Instruktor")
    first_time = models.BooleanField(default=True, verbose_name="Nowo zarejestrowany")

    def __str__(self):
        return self.user.first_name


class RoomsAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "address", "description")


class Rooms(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa salki")
    address = models.CharField(max_length=254, blank=True, verbose_name="Adres",
                               help_text="np. ul.Krajobrazowa 8/1, 00-001, Twoje Miasto")
    description = models.CharField(max_length=254, blank=True, verbose_name="Opis")
    user = models.ManyToManyField("self", symmetrical=False, through="Reservations", related_name="Użytkownik")

    def __str__(self):
        return self.name


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "teacher", "rooms", "reservation_time_start",
                    "reservation_time_end", "activities_type")


class Reservations(models.Model):
    user = models.ForeignKey(User, related_name="student", verbose_name="Kursant")
    teacher = models.ForeignKey(User, related_name="teacher", verbose_name="Instruktor")
    rooms = models.ForeignKey(Rooms)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, verbose_name="Data", help_text="DD-MM-RRRR")
    reservation_time_start = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Rezerwacja od")
    reservation_time_end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Rezerwacja do")
    activities_type = models.CharField(choices=ACTIVITIES, max_length=15,
                                       default="Ćwiczenia", verbose_name="Rodzaj zajęć")

    def __str__(self):
        return self.user.first_name
