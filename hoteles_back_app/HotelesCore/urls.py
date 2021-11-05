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
    url(r'^check_rooms/(?P<pk_hotel>[0-9]+)/(?P<nro_guests>[0-9]+)$',roomsAvailablesByHotel),
    path('check_in/',CheckInBooking),
    #url(r'^check_out/(?P<pk>[0-9]+)$',CheckOutBooking)
]