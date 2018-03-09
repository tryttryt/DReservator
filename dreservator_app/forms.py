from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput, EmailInput

from dreservator_app.models import Users, Rooms, Reservations


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = "username", "password", "confirm_password", "first_name", "last_name", "email"
        widgets = {'password': PasswordInput, 'email': EmailInput}

        def clean(self):
            cleaned_data = super(RegisterForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError("Wprowadzone hasła nie są zgodne")


class RecoverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "email",
        widgets = {'email': EmailInput}
        #  exclude = ['available_from']


class AddUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "address", "phone", "is_instructor"


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = "name", "address", "description"


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):  # https://www.djangosnippets.org/snippets/1202/
    input_type = 'time'


class AddReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = "__all__"
        widgets = {'date': DateInput(),
                   'reservation_time_start': TimeInput(),
                   'reservation_time_end': TimeInput(),
                   }


class SearchUserForm(forms.Form):
    last_name = forms.CharField(label="Wpisz nazwisko ", max_length=100)


class SearchReservationForm(forms.Form):
    date = forms.DateField(label="Wybierz datę ", widget=DateInput())
