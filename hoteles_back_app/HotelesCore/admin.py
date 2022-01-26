from django.contrib import admin
from HotelesCore.models import *
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking)
admin.site.register(Image) # esto es un comment
admin.site.register(Publicidad) # esto es un comment
admin.site.register(PaqueteTuristico) # esto es un comment
admin.site.register(Puntuacion)
admin.site.register(Detalle)
#admin.site.register(Puntuaciones) # esto es un comment



