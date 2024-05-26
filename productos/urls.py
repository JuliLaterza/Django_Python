from django.urls import path
from . import  views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name = 'index'),
    path(
        '<int:producto_id>',
         views.detalle,
         name='producto_detalle'
    ),
]