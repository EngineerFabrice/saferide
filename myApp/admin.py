from django.contrib import admin
from .models import User, Admin, Location, Driver, Booking, Feedback

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Location)
admin.site.register(Driver)
admin.site.register(Booking)
admin.site.register(Feedback)

