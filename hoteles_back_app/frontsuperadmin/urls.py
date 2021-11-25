from django.conf.urls import url
from django.views.generic.base import TemplateView
from frontsuperadmin import *

urlpatterns = [
url(r'^.*', TemplateView.as_view(template_name="frontsuperadmin/home.html"), name="home")
]