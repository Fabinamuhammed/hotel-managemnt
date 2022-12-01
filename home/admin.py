from django.contrib import admin

# Register your models here.

from .models import User
from .models import Hotel
from .models import rooms
from .models import Booking

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(rooms)
admin.site.register(Booking)
