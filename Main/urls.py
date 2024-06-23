from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("copy",views.copy,name="copy"),
    path("paste",views.paste,name="paste"),
]