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
    path('check_in/',CheckInBooking),
    path('check_out/',CheckOutBooking),
    path('extend_booking/',update_checkout),
    path('images/', home_view ),
    path("puntuacion/",puntuacion),
    path("paquetes_turisticos/",paquetesListView),
    path("publicidad/",publicidad_list_view),
    #url(r'^check_out/(?P<pk>[0-9]+)$',CheckOutBooking)
]