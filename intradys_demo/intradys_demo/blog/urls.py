from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("api/get_color_setting", views.get_color_setting, name="get_color_setting"),
    path("api/set_color_setting", views.set_color_setting, name="set_color_setting")

]