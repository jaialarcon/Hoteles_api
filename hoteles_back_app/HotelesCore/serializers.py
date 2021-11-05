from rest_framework import serializers

from HotelesCore.models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id_hotel', 'name','address','crated_at','updated_at')

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id_room_type', 'name', 'personas', 'cocina', 'cama', 'wifi', 'lavanderia', 'desayuno', 'description','crated_at','updated_at')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('hotel', 'room', 'user','crated_at','updated_at','begin_at','ends_at','ends')