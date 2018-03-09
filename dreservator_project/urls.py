"""drservator_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dreservator_app.views import mainview, usersview, roomsview, reservationsview, AddUserView, AddRoomView, \
    AddReservationView, Login, mylogout, Register, PassRecovery, EditUserView, deactivateuser, EditRoomView, deleteroom, \
    EditReservationView, deletereservation, SearchUserView, SearchReservationView, contact


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainview, name='mainview'),

    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^recover/$', PassRecovery.as_view(), name='recover'),
    url(r'^logout/$', mylogout, name='mylogout'),
    url(r'^users/$', usersview, name='usersview'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^add_user/$', AddUserView.as_view(), name='add_user'),
    url(r'^edit_user/(?P<id>(\d)+)/$', EditUserView.as_view(), name='edit_user'),
    url(r'^delete_user/(?P<id>(\d)+)/$', deactivateuser, name='delete_user'),
    url(r'^search_user/$', SearchUserView.as_view(), name='search_user'),

    url(r'^add_room/$', AddRoomView.as_view(), name='add_room'),
    url(r'^rooms/$', roomsview, name='roomsview'),
    url(r'^edit_room/(?P<id>(\d)+)/$', EditRoomView.as_view(), name='edit_room'),
    url(r'^delete_room/(?P<id>(\d)+)/$', deleteroom, name='delete_room'),

    url(r'^reservations/$', reservationsview, name='reservationsview'),
    url(r'^add_reservation/$', AddReservationView.as_view(), name='add_reservation'),
    url(r'^edit_reservation/(?P<id>(\d)+)/$', EditReservationView.as_view(), name='edit_reservation'),
    url(r'^delete_reservation/(?P<id>(\d)+)/$', deletereservation, name='delete_reservation'),
    url(r'^search_reservation/$', SearchReservationView.as_view(), name='search_reservation'),

    url(r'^contact/$', contact, name='contact'),
]
