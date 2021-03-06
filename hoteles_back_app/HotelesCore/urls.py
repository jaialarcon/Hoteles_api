from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls import url

urlpatterns = [
    path("hotels/",HotelListView),
    #url(r'^room_types/',RoomtypeListView),
    url(r'^room_types/(?P<pk>[0-9]+)$',RoomtypeListView),
    url(r'^user_type/(?P<pk>[0-9]+)$',UserType),
    url(r'^bookings_hotel/(?P<pk_hotel>[0-9]+)$',bookings_by_hotel),
    url(r'^check_rooms/(?P<pk_hotel>[0-9]+)/(?P<nro_guests>[0-9]+)$',roomsAvailablesByHotel),
    url(r'^bookings_user/(?P<pk_hotel>[0-9]+)/(?P<pk_usuario>[0-9]+)$',bookings_by_hotel_by_user),
    url(r'^rooms_hotel/(?P<pk_hotel>[0-9]+)$',rooms_by_hotel),
    url(r'^roomtype_room/(?P<pk_room>[0-9]+)$',roomtype_by_hotel),
    url(r'^get_room/(?P<pk_room>[0-9]+)$',room_by_id),
    path('check_in/',CheckInBooking),
    path('booking_cost/',update_booking_addcost),
    path('booking_setcosts/',update_booking_setcost),
    path('cancel_booking/',cancelBooking),
    path('check_out/',CheckOutBooking),
    path('extend_booking/',update_checkout),
    path('images/', Images ),
    path("puntuacion/",puntuacion),
    path("paquetes_turisticos/",paquetesListView),
    path("publicidad/",publicidad_list_view),
    path("detalle/",detalle_list_view),
    url(r'^publicidad_hotel/(?P<pk_hotel>[0-9]+)$',publicidad_by_hotel),
    url(r'^paquete_hotel/(?P<pk_hotel>[0-9]+)$',paquetes_by_hotel),
    url(r'^puntuaciones_hotel/(?P<pk_hotel>[0-9]+)$',puntuacion_by_hotel),
    url(r'^detalle_reserva/(?P<booking>[0-9]+)$',detalle_by_booking),
]