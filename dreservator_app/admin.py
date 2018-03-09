from django.contrib import admin
from dreservator_app.models import Users, Rooms, Reservations, UsersAdmin, RoomsAdmin, ReservationsAdmin

admin.site.register(Users, UsersAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Reservations, ReservationsAdmin)
