from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls import url

urlpatterns = [
    path("hotels/",HotelListView),
    path('room_types/',RoomtypeListView),
    path('check_in/',CheckInBooking),
    #url(r'^check_out/(?P<pk>[0-9]+)$',CheckOutBooking)
]