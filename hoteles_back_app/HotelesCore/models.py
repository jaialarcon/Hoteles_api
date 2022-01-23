
from django.db import models
from django.utils.translation import pgettext_lazy
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    address = models.CharField(max_length=500,unique=True,verbose_name=pgettext_lazy('Hotel','direccion'))

    def __str__(self):
        return self.name
    class Meta:
        # Define the database table
        db_table = 'hotel'
        ordering = ['id_hotel']
        verbose_name = pgettext_lazy('Hotel', 'Hotel')
        verbose_name_plural = pgettext_lazy('Hotel', 'Hotels')

class RoomType(models.Model):
    id_room_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True,verbose_name=pgettext_lazy('RoomType','name'))
    personas = models.PositiveIntegerField(default=0)
    ninios = models.PositiveIntegerField(default=0)
    cocina = models.BooleanField(default=False)
    cama = models.PositiveIntegerField(default=0)
    wifi = models.BooleanField(default=False)
    lavanderia = models.BooleanField(default=False)
    desayuno = models.BooleanField(default=False)
    description = models.TextField(blank=True,verbose_name=pgettext_lazy('RoomType','description'))
    crated_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        # Define the database table
        db_table = 'hotels_roomtypes'
        ordering = ['id_room_type']
        verbose_name = pgettext_lazy('RoomType', 'Room type')
        verbose_name_plural = pgettext_lazy('RoomType', 'Room types')

    def __str__(self):
        return self.name

class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel',on_delete=models.PROTECT,verbose_name=pgettext_lazy('Room','id_hotel'))
    name = models.CharField(max_length=255,verbose_name=pgettext_lazy('Room','name'))
    description = models.TextField(blank=True,verbose_name=pgettext_lazy('Room','description'))
    room_type = models.ForeignKey('RoomType',on_delete=models.PROTECT,verbose_name=pgettext_lazy('Room','id_room_type'))
    phone1 = models.CharField(max_length=255,blank=True,verbose_name=pgettext_lazy('Room','phone 1'))
    seats_base = models.PositiveIntegerField(default=1,verbose_name=pgettext_lazy('Room','seats base'))
    seats_additional = models.PositiveIntegerField(default=0,verbose_name=pgettext_lazy('Room','seats additional'))
    booked = models.BooleanField(default=False,verbose_name=pgettext_lazy('Room','booked Room'))
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        # Define the database table
        db_table = 'hotels_rooms'
        ordering = ['id_room']
        verbose_name = pgettext_lazy('Room', 'Room')
        verbose_name_plural = pgettext_lazy('Room', 'Rooms')

    def __str__(self):
        return '{HOTEL} - {NAME}'.format(HOTEL=self.hotel.name, NAME=self.name)

class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Booking', 'id_hotel'))
    room = models.ForeignKey('Room', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Booking', 'room'))
    user = models.IntegerField(default=0,verbose_name='user')
    cedula= models.CharField(max_length=15,default='0999999999')
    status = models.CharField(max_length=255,default='activa',verbose_name=pgettext_lazy('Booking','status'))
    costo_booking = models.DecimalField(default=0, max_digits=10, decimal_places=2 )
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    begin_at = models.DateTimeField(default=datetime.now())
    ends_at = models.DateTimeField()
    ends = models.BooleanField(default=False,verbose_name=pgettext_lazy('Room','ends Booking'))
    class Meta:
        # Define the database table
        db_table = 'hotels_rooms_booking'
        ordering = ['id_booking']
        verbose_name = pgettext_lazy('Booking', 'Booking')
        verbose_name_plural = pgettext_lazy('Booking', 'Bookings')

    def __str__(self):
        return '{USER} - {ROOM}'.format(USER=self.user, ROOM=self.room)

class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image_field = models.ImageField()
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    class Meta:
        # Define the database table
        db_table = 'images'
        ordering = ['id_image']
        verbose_name = pgettext_lazy('image', 'table')
        verbose_name_plural = pgettext_lazy('Image', 'Images')

    def __str__(self):
        return '{ID} - {NAME}'.format(ID=self.id_image, NAME=self.name)

class PaqueteTuristico(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    paquete = models.CharField(max_length=255)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Booking', 'id_hotel'))
    costo = models.DecimalField(default=0, max_digits=10, decimal_places=2 )
    personas = models.PositiveIntegerField(default=0)
    cedula = models.CharField(max_length=10, verbose_name=pgettext_lazy('Paquete', 'cedula'))
    cliente = models.CharField(max_length=255)
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    paquete_date = models.DateTimeField(default=datetime.now())
    paquete_ends_at = models.DateTimeField()
    estado = models.CharField(max_length=25)
    class Meta:
        # Define the database table
        db_table = 'hotels_paquetes_turisticos'
        ordering = ['id_paquete']
        verbose_name = pgettext_lazy('Paquete', 'turistico')
        verbose_name_plural = pgettext_lazy('Paquetes', 'Turisticos')

    def __str__(self):
        return '{ID} - {PAQUETE}'.format(ID=self.id_paquete, PAQUETE=self.paquete)

class Puntuaciones(models.Model):
    id_puntuacion = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Puntuaciones', 'id_hotel'))
    usuario = models.IntegerField(default=0,verbose_name='user')
    puntuacion = models.DecimalField(decimal_places=2,default=0,max_digits=4)
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    class Meta:
        # Define the database table
        db_table = 'hotels_puntuaciones'
        ordering = ['id_puntuacion']
        verbose_name = pgettext_lazy('Puntuacion', 'hotel')
        verbose_name_plural = pgettext_lazy('Puntuaciones', 'hoteles')

    def __str__(self):
        return '{ID} - {PUNTUACION}'.format(ID=self.id_puntuacion, PUNTUACION=self.puntuacion)

class Publicidad(models.Model):
    id_public = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Puntuaciones', 'id_hotel'))
    servicio = models.CharField(max_length=255)
    detalle = models.CharField(max_length=255)
    costo_pub = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    publicidad_date = models.DateTimeField(default=datetime.now())
    publicidad_ends_at = models.DateTimeField()
    estado = models.CharField(max_length=25)
    class Meta:
        # Define the database table
        db_table = 'hotels_publicidad'
        ordering = ['id_public']
        verbose_name = pgettext_lazy('Hotel','Publicidad')
        verbose_name_plural = pgettext_lazy('Hoteles', 'Publicidades')

    def __str__(self):
        return '{ID} - {SERVICE}'.format(ID=self.id_public, SERVICE=self.servicio)


class Puntuacion(models.Model):
    id_punt = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Puntuaciones', 'id_hotel'))
    user = models.IntegerField(default=0,verbose_name='user')
    puntu = models.DecimalField(decimal_places=2,default=0,max_digits=4)
    crated_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    class Meta:
        # Define the database table
        db_table = 'Puntuation'
        ordering = ['id_punt']
        verbose_name = pgettext_lazy('Puntuacion', 'hotel')
        verbose_name_plural = pgettext_lazy('Puntuaciones')

    def __str__(self):
        return '{ID} - {PUNTUACION}'.format(ID=self.id_punt, PUNTUACION=self.puntu)
