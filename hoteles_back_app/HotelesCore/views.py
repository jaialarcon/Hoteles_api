from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from django.contrib.auth import get_user_model

from .user.models import User


@csrf_exempt
@api_view(['GET', 'POST'])
def HotelListView(request):
    if request.method == 'GET':
        model = Hotel.objects.all()
        serializer = HotelSerializer(model, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def RoomtypeListView(request,pk):
    if request.method == 'GET':
        id= pk
        try:
            model = RoomType.objects.filter(id_room_type = id)
            print("Hola")
        except RoomType.DoesNotExist:
            print("Exception")
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = RoomTypeSerializer(model, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def CheckInBooking(request):
    #hotel_id = request.data['hotel']
    #room = request.data['room']
    #user = request.data['user']
    #my_date = date(2021, 3, 2)

    begin_booking_date = request.data["begin_at"].split(" ")[0].split("-")
    year = int(begin_booking_date[0])
    month = int(begin_booking_date[1])
    day =  int(begin_booking_date[2])
    begin_date = datetime(year, month, day, 0, 0, 0, 0)
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    end_date = datetime(yearE,monthE,dayE,0,0,0,0)
    hotel_id = request.data["id_hotel"]
    room = request.data["room"]
    user = request.data["user"]
    s_booking_room = {
        "data": {
            'message': 'Hotel does not exists'
        }

    }
    if request.method == 'POST':
        if Hotel.objects.filter(id_hotel=hotel_id).exists():
            if Room.objects.filter(id_room= room).exists():
                current_room = Room.objects.get(id_room= room)
                print("si hay habitación")
                is_booked = current_room.booked
                print(is_booked)
                if not is_booked:
                    print("disponible")
                    #"print(request.data)
                    data ={
                            "hotel": hotel_id,
                            "room": room,
                            "user": user,
                            "begin_at": begin_date,
                            "ends_at": end_date,
                            "ends": False,
                    }
                    s_booking_room = BookingSerializer(data=data)
                    print(s_booking_room)
                    #print(s_booking_room.is_valid())
                    if s_booking_room.is_valid():
                        print(s_booking_room.is_valid())
                        print(s_booking_room)
                        print("VALIDO")
                        print("No está ocupada")
                        current_room.booked = True
                        current_room.save(force_update=True)
                        s_booking_room.save()
                        return Response(s_booking_room.data, status=status.HTTP_201_CREATED)


                else :
                    s_booking_room = {
                        'data':{
                            'message': 'Room is not available'
                        }

                    }
                    return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)


        return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def CheckOutBooking(request):
    #hotel_id = request.data['hotel']
    #room = request.data['room']
    #user = request.data['user']
    #my_date = date(2021, 3, 2)
    id_bookinig = int(request.data["booking"])
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    end_date = datetime(yearE,monthE,dayE,0,0,0,0)
    s_booking_room = {
        "data": {
            'message': 'Booking does not exists'
        }

    }
    if request.method == 'POST':
        print("Post")
        if Booking.objects.filter(id_booking=id_bookinig).exists():
            print("Existe booking")
            current_booking = Booking.objects.get(id_booking=id_bookinig)
            current_booking.ends_at = end_date
            current_booking.updated_at = end_date
            current_booking.ends = True
            room = Room.objects.get(id_room=current_booking.room.id_room)
            room.booked = False
            current_booking.save(force_update=True)
            room.save(force_update=True)
            s_booking_room = {
                "data": {
                    'message': 'Registro Actualizado correctamente, se ha realizado checkout'
                }
            }
        else:
            s_booking_room = {
                'data': {
                    'message': 'error to checkout Booking does not exists'
                }

            }
            return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

        return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET'])
def roomsAvailablesByHotel(request,pk_hotel,nro_guests):
    rooms = Room.objects.filter(hotel= pk_hotel)
    data = []
    for room in rooms:
        print("En el for")
        room_type = room.room_type
        infoHotelRoom = {
            "id_hotel": pk_hotel,
            "id_room": room.id_room,
            "room_name": room.name,
            "price_room": room.seats_base,
            "additional_price_room": room.seats_additional,
            "room_detail":{
                "id": room_type.id_room_type,
                "name": room_type.name,
                "description": room_type.description,
                "guests_number": room_type.personas,
                "breakfast": room_type.desayuno,
                "wifi": room_type.wifi,
                "kitchen": room_type.cocina,
                "beds_number":room_type.cama,
                "lawndry": room_type.lavanderia
            }

        }
        print(infoHotelRoom)
        print(room_type.personas)
        print(nro_guests)
        is_booked= room.booked
        if room_type.personas >= int(nro_guests) and not is_booked:
            print("Si")
            data.append(infoHotelRoom)

    return Response(data,status=status.HTTP_201_CREATED)
@csrf_exempt
@api_view(['GET'])
def UserType(request,pk):
    user= User.objects.get(id=pk)
    isAdmin = user.is_staff
    isSuperAdmin = user.is_superuser
    isClient = False
    data= []
    resp= ""
    if(isAdmin and not isSuperAdmin):
        resp = "Admin"
    elif(isSuperAdmin and not isAdmin):
        resp = "SuperAdmin"
    elif(not isAdmin and not isSuperAdmin):
        isClient = True
        resp = "Client"
    else:
        resp = "SuperAdmin"
    resdata={
        "user_type": resp,
        "is_client": isClient
    }
    data.append(resdata)
    return Response(data, status=status.HTTP_201_CREATED)


