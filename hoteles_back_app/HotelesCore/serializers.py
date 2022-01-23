from rest_framework import serializers

from HotelesCore.models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id_hotel', 'name','address')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id_room', 'hotel', 'name', 'description', 'room_type', 'phone1', 'seats_base', 'seats_additional', 'booked')

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id_room_type', 'name', 'personas','ninios', 'cocina', 'cama', 'wifi', 'lavanderia', 'desayuno', 'description')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id_booking','hotel', 'room', 'user','cedula','costo_booking','status','begin_at','ends_at','ends')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields= ('id_image','name','image_field')


class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteTuristico
        fields = ('id_paquete', 'paquete', 'hotel','costo','personas','cedula','cliente','paquete_date','paquete_ends_at','estado')


class PuntuacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntuacion
        fields = ('id_punt', 'hotel', 'user','puntu')


class PublicidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = ('id_public',"hotel", 'servicio','detalle','costo_pub','publicidad_date','publicidad_ends_at','estado')