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

from django.shortcuts import render
from .forms import ImageForm
from .models import Image


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
@api_view(['GET', 'POST'])
def Images(request):
    if request.method == 'GET':
        model = Image.objects.all()
        serializer = ImageSerializer(model, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def RoomtypeListView(request, pk):
    if request.method == 'GET':
        id = pk
        try:
            model = RoomType.objects.filter(id_room_type=id)
            print("Hola")
        except RoomType.DoesNotExist:
            print("Exception")
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RoomTypeSerializer(model, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def CheckInBooking(request):
    # hotel_id = request.data['hotel']
    # room = request.data['room']
    # user = request.data['user']
    # my_date = date(2021, 3, 2)

    begin_booking_date = request.data["begin_at"].split(" ")[0].split("-")
    year = int(begin_booking_date[0])
    month = int(begin_booking_date[1])
    day = int(begin_booking_date[2])
    begin_date = datetime(year, month, day, 0, 0, 0, 0)
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    costo_booking = float(request.data["costo_booking"])
    cedula = request.data['cedula']
    nombre = request.data['nombre']
    apellido = request.data['apellido']
    telefono = request.data['telefono']
    email = request.data['email']
    end_date = datetime(yearE, monthE, dayE, 0, 0, 0, 0)
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
            if Room.objects.filter(id_room=room).exists():
                current_room = Room.objects.get(id_room=room)
                print("si hay habitación")
                is_booked = current_room.booked
                print(is_booked)
                if not is_booked:
                    print("disponible")
                    # "print(request.data)
                    data = {
                        "hotel": hotel_id,
                        "room": room,
                        "user": user,
                        "cedula": cedula,
                        "nombre": nombre,
                        "apellido": apellido,
                        "telefono": telefono,
                        "email" : email,
                        "costo_booking": costo_booking,
                        "begin_at": begin_date,
                        "ends_at": end_date,
                        "ends": False,
                    }
                    s_booking_room = BookingSerializer(data=data)
                    print(s_booking_room)
                    # print(s_booking_room.is_valid())
                    if s_booking_room.is_valid():
                        print(s_booking_room.is_valid())
                        print(s_booking_room)
                        print("VALIDO")
                        print("No está ocupada")
                        current_room.booked = True
                        current_room.save(force_update=True)
                        s_booking_room.save()
                        return Response(s_booking_room.data, status=status.HTTP_201_CREATED)


                else:
                    s_booking_room = {
                        'data': {
                            'message': 'Room is not available'
                        }

                    }
                    return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

        return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
def CheckOutBooking(request):
    # hotel_id = request.data['hotel']
    # room = request.data['room']
    # user = request.data['user']
    # my_date = date(2021, 3, 2)
    id_bookinig = int(request.data["booking"])
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    end_date = datetime(yearE, monthE, dayE, 0, 0, 0, 0)
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
            current_booking.status = 'terminada'
            room = Room.objects.get(id_room=current_booking.room.id_room)
            room.booked = False
            room.seats_additional =0
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
def roomsAvailablesByHotel(request, pk_hotel, nro_guests):
    rooms = Room.objects.filter(hotel=pk_hotel)
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
            "room_detail": {
                "id": room_type.id_room_type,
                "name": room_type.name,
                "description": room_type.description,
                "guests_number": room_type.personas,
                "breakfast": room_type.desayuno,
                "wifi": room_type.wifi,
                "kitchen": room_type.cocina,
                "beds_number": room_type.cama,
                "lawndry": room_type.lavanderia
            }

        }
        print(infoHotelRoom)
        print(room_type.personas)
        print(nro_guests)
        is_booked = room.booked
        if room_type.personas >= int(nro_guests) and not is_booked:
            print("Si")
            data.append(infoHotelRoom)

    return Response(data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def UserType(request, pk):
    user = User.objects.get(id=pk)
    isAdmin = user.is_staff
    isSuperAdmin = user.is_superuser
    isClient = False
    data = []
    resp = ""
    if (isAdmin and not isSuperAdmin):
        resp = "Admin"
    elif (isSuperAdmin and not isAdmin):
        resp = "SuperAdmin"
    elif (not isAdmin and not isSuperAdmin):
        isClient = True
        resp = "Client"
    else:
        resp = "SuperAdmin"
    resdata = {
        "user_type": resp,
        "is_client": isClient
    }
    data.append(resdata)
    return Response(data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET', 'POST'])
def home_view(request):
    context = {}
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("image_field")
            obj = Image.objects.create(
                name=name,
                image_field=img
            )
            obj.save()
            print(obj)
    else:
        form = ImageForm()
    context['form'] = form
    return render(request, "image.html", context)


@csrf_exempt
@api_view(['GET'])
def bookings_by_hotel(request, pk_hotel):
    bookings = Booking.objects.filter(hotel=pk_hotel)
    #data = [res for res in bookings]
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def bookings_by_hotel_by_user(request, pk_hotel, pk_usuario):
    bookings = Booking.objects.filter(hotel=pk_hotel)
    byUser = bookings.filter(user=pk_usuario)
    serializer = BookingSerializer(byUser, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])

def roomtype_by_hotel(request,pk_room):
    room = Room.objects.get(id_room=pk_room)
    room_type = room.room_type
    data = [room_type]
    serializer = RoomTypeSerializer(data,many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])

def room_by_id(request,pk_room):
    room = Room.objects.get(id_room= pk_room)
    data = [room]
    serializer = RoomSerializer(data,many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST'])
def puntuacion(request):
    if request.method == 'GET':
        model = Puntuacion.objects.all()
        serializer = PuntuacionesSerializer(model, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PuntuacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET'])

def puntuacion_by_hotel(request,pk_hotel):
    todas = Puntuacion.objects.all()
    por_hotel = todas.filter(hotel=pk_hotel)
    #data = [puntuacion]
    serializer = PuntuacionesSerializer(por_hotel,many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST'])
def paquetesListView(request):
    if request.method == 'GET':
        model = PaqueteTuristico.objects.all()
        serializer = PaqueteSerializer(model, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaqueteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])

def paquetes_by_hotel(request,pk_hotel):
    todas = PaqueteTuristico.objects.all()
    paquetes_hotel = todas.filter(hotel=pk_hotel)
    serializer = PaqueteSerializer(paquetes_hotel,many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', 'POST'])
def publicidad_list_view(request):
    if request.method == 'GET':
        model = Publicidad.objects.all()
        serializer = PublicidadSerializer(model, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PublicidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@csrf_exempt
@api_view(['GET'])

def publicidad_by_hotel(request,pk_hotel):
    todas = Publicidad.objects.all()
    por_hotel = todas.filter(hotel= pk_hotel)
    #data = [publicidad]
    serializer = PublicidadSerializer(por_hotel,many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def update_checkout(request):
    # hotel_id = request.data['hotel']
    # room = request.data['room']
    # user = request.data['user']
    # my_date = date(2021, 3, 2)
    id_bookinig = int(request.data["booking"])
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    end_date = datetime(yearE, monthE, dayE, 0, 0, 0, 0)
    s_booking_room = {
        "data": {
            'message': 'Booking does not exists'
        }

    }
    if request.method == 'POST':
        print("Post")
        if Booking.objects.filter(id_booking=id_bookinig).exists() and not Booking.objects.get(id_booking=id_bookinig).ends:
            print("Existe booking")
            current_booking = Booking.objects.get(id_booking=id_bookinig)
            current_booking.ends_at = end_date
            current_booking.updated_at = end_date
            current_booking.status = 'activa'
            current_booking.save(force_update=True)
            s_booking_room = {
                "data": {
                    'message': 'Registro Actualizado correctamente, se ha extendido su reserva'
                }
            }
            return Response(s_booking_room.get("data"), status=status.HTTP_200_OK)
        else:
            s_booking_room = {
                'data': {
                    'message': 'error to extends Booking does not exists'
                }

            }
            return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

        return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['GET'])
def rooms_by_hotel(request,pk_hotel):
    rooms = Room.objects.filter(hotel=pk_hotel)
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
            "room_detail": {
                "id": room_type.id_room_type,
                "name": room_type.name,
                "description": room_type.description,
                "guests_number": room_type.personas,
                "ninios": room_type.ninios,
                "breakfast": room_type.desayuno,
                "wifi": room_type.wifi,
                "kitchen": room_type.cocina,
                "beds_number": room_type.cama,
                "lawndry": room_type.lavanderia
            }

        }
        print(infoHotelRoom)
        print(room_type.personas)
        print("Si")
        data.append(infoHotelRoom)
    return Response(data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['POST'])
def update_booking_addcost(request):
    # hotel_id = request.data['hotel']
    # room = request.data['room']
    # user = request.data['user']
    # my_date = date(2021, 3, 2)
    id_bookinig = int(request.data["booking"])
    #end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    #yearE = int(end_booking_date[0])
    #monthE = int(end_booking_date[1])
    #dayE = int(end_booking_date[2])
    #end_date = datetime(yearE, monthE, dayE, 0, 0, 0, 0)
    seats_additional = int(request.data["costo_adicional"])
    s_booking_room = {
        "data": {
            'message': 'Booking does not exists'
        }

    }
    if request.method == 'POST':
        print("Post")
        if Booking.objects.filter(id_booking=id_bookinig).exists() and not Booking.objects.get(id_booking=id_bookinig).ends:
            print("Existe booking")
            current_booking = Booking.objects.get(id_booking=id_bookinig)
            #current_booking.ends_at = end_date
            #current_booking.updated_at = end_date
            #current_booking.status = 'activa'
            current_booking.costo_booking += seats_additional
            room = current_booking.room
            room.seats_additional += seats_additional
            room.save(force_update=True)
            current_booking.save(force_update=True)
            s_booking_room = {
                "data": {
                    'message': 'Registro Actualizado correctamente, se ha realizado costo adicional'
                }
            }
            return Response(s_booking_room.get("data"), status=status.HTTP_200_OK)
        else:
            s_booking_room = {
                'data': {
                    'message': 'error to checkout Booking does not exists'
                }

            }
            return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

        return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def cancelBooking(request):
    # hotel_id = request.data['hotel']
    # room = request.data['room']
    # user = request.data['user']
    # my_date = date(2021, 3, 2)
    id_bookinig = int(request.data["booking"])
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
            current_booking.ends = True
            current_booking.status = 'cancelada'
            room = current_booking.room
            room.booked = False
            room.seats_additional =0
            current_booking.save(force_update=True)
            room.save(force_update=True)
            s_booking_room = {
                "data": {
                    'message': 'Registro Actualizado correctamente, se ha cancelado correctamente su reserva'
                }
            }
            return Response(s_booking_room.get("data"), status=status.HTTP_200_OK)
        else:
            s_booking_room = {
                'data': {
                    'message': 'error to checkout Booking does not exists'
                }

            }
            return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)

        return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET', 'POST'])
def detalle_list_view(request):
    if request.method == 'GET':
        model = Detalle.objects.all()
        serializer = DetalleSerializer(model, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DetalleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def detalle_by_booking(request, booking):
    todas = Detalle.objects.all()
    por_reserva = todas.filter(booking=booking)
    # data = [publicidad]s
    serializer = DetalleSerializer(por_reserva, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
