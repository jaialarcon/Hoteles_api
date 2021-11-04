from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls import url

urlpatterns = [
    path("hotels/",HotelListView),
    #url(r'^room_types/',RoomtypeListView),
    url(r'^room_types/(?P<pk>[0-9]+)$',RoomtypeListView),
    path('check_in/',CheckInBooking),
    #url(r'^check_out/(?P<pk>[0-9]+)$',CheckOutBooking)
]