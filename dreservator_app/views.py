from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from dreservator_app.models import Users, Rooms, Reservations
from .forms import AddUserForm, AddRoomForm, AddReservationForm, RegisterForm, RecoverForm, SearchUserForm, \
    SearchReservationForm


def mainview(request):
    return render(request, 'index.html')
    # return redirect(reverse('mainview'))


def usersview(request):
    return render(request, 'users.html')
    # return redirect(request(reverse('usersview')))


def roomsview(request):
    return render(request, 'rooms.html')
    # return redirect(reverse('roomsview'))


def reservationsview(request):
    return render(request, 'reservations.html')
    # return redirect(reverse('reservationsview'))


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            url = request.GET.get("next")
            if url:
                return redirect(url)
            return redirect("/")
        return HttpResponse("Niepoprawny login lub hasło")
# return redirect(reverse('login'))


def mylogout(request):
    logout(request)
    return redirect(reverse('mainview'))


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            extenduser = Users.objects.create(user_id=user.id, is_instructor=False, first_time=True)

        return redirect("/")
        # return redirect(reverse('main'))


class PassRecovery(View):
    def get(self, request):
        form = RecoverForm()
        return render(request, "recover.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if email == user.email:
                return ('Sprawdź skrzynkę, za chwilę otrzymasz e-mail z instrukcją odzyskiwania hasła')
            else:
                return ("Podany e-mail nie istnieje w naszej bazie")

        return redirect("/")


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        userform = RegisterForm()
        return render(request, "add_user.html", {'form': form, "userform": userform})

    def post(self, request):
        form = AddUserForm(request.POST)
        userform = RegisterForm(request.POST)
        if all((form.is_valid(), userform.is_valid())):
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            first_name = userform.cleaned_data['first_name']
            last_name = userform.cleaned_data['last_name']
            email = userform.cleaned_data['email']
            user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email)
            extendeduser = form.save(commit=False)
            extendeduser.user_id = user.pk
            extendeduser.save()

        return redirect(reverse('usersview'))


class SearchUserView(View):

    def get(self, request):
        form = SearchUserForm()
        return render(request, "search_user.html", {'form': form})

    def post(self, request):
        form = SearchUserForm(request.POST)

        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            students = User.objects.filter(last_name__icontains=last_name)  # __istartswith
            student_id = User.objects.filter(last_name__icontains=last_name).values('id')
            reservation = Reservations.objects.filter(user_id=student_id)
        return render(request, "search_user.html", {'form': form,
                                                    'students': students,
                                                    'reservation': reservation })


class EditUserView(View):
    def get(self, request, id):
        u = User.objects.get(pk=id)
        form = AddUserForm(instance=u.users)
        userform = RegisterForm(instance=u)
        return render(request, "add_user.html", {'form': form, "userform": userform})

    def post(self, request, id):
        u = User.objects.get(pk=id)
        form = AddUserForm(request.POST, instance=u.users)
        userform = RegisterForm(request.POST, instance=u)
        if all((form.is_valid(), userform.is_valid())):
            form.save()
            userform.save()
            return render(request, "users.html")


def deactivateuser(request, id):
    u = User.objects.get(pk=id)
    u.is_active = False
    u.save()
    return render(request, "users.html")


class AddRoomView(View):
    def get(self, request):
        form = AddRoomForm()
        return render(request, "add_room.html", {'form': form})

    def post(self, request):
        form = AddRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            r = Rooms.objects.create(name=name,
                                     address=address,
                                     description=description)
        return redirect(reverse('roomsview'))


class EditRoomView(View):
    def get(self, request, id):
        r = Rooms.objects.get(pk=id)
        form = AddRoomForm(instance=r)
        return render(request, "add_room.html", {'form': form})

    def post(self, request, id):
        r = Rooms.objects.get(pk=id)
        f = AddRoomForm(request.POST, instance=r)
        if f.is_valid():
            f.save()
            return render(request, "rooms.html")


def deleteroom(request, id):
    Rooms.objects.get(pk=id).delete()
    return render(request, "rooms.html")


class AddReservationView(View):
    def get(self, request):
        form = AddReservationForm()
        return render(request, "add_reservation.html", {'form': form})

    def post(self, request):
        form = AddReservationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            teacher = form.cleaned_data['teacher']
            rooms = form.cleaned_data['rooms']
            date = form.cleaned_data['date']
            reservation_time_start = form.cleaned_data['reservation_time_start']
            reservation_time_end = form.cleaned_data['reservation_time_end']
            activities_type = form.cleaned_data['activities_type']
            r = Reservations.objects.create(user=user, teacher=teacher, rooms=rooms, date=date,
                                            reservation_time_start=reservation_time_start,
                                            reservation_time_end=reservation_time_end,
                                            activities_type=activities_type)
        return redirect(reverse('reservationsview'))
        # return redirect("/reservations/")
        # return redirect("/rooms/%s" % room[id])


class SearchReservationView(View):

    def get(self, request):
        form = SearchReservationForm()
        return render(request, "search_reservation.html", {'form': form})

    def post(self, request):
        form = SearchReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            reservat = Reservations.objects.filter(date=date)  # __contains
        return render(request, "search_reservation.html", {'form': form, 'reservat': reservat})


class EditReservationView(View):
    def get(self, request, id):
        r = Reservations.objects.get(pk=id)
        form = AddReservationForm(instance=r)
        return render(request, "add_room.html", {'form': form})

    def post(self, request, id):
        r = Reservations.objects.get(pk=id)
        f = AddReservationForm(request.POST, instance=r)
        if f.is_valid():
            f.save()
            return render(request, "reservations.html")


def deletereservation(request, id):
    Reservations.objects.get(pk=id).delete()
    return render(request, "reservations.html")


def contact(request):
    return render(request, "contact.html")

#  @login_required(login_url="/login/") - decorator for future authentication

