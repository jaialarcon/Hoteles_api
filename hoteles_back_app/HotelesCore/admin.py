from django.contrib import admin
from HotelesCore.models import *
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking)