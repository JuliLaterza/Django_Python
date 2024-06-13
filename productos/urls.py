from django.urls import path
from . import  views
from django.contrib import admin


app_name = 'producto' #Por convención de Django.

urlpatterns = [
    path('', views.index, name = 'index'),
    path('formulario',views.formulario, name='formulario'),
    path(
        '<int:producto_id>',
         views.detalle,
         name='detalle'
    ),
]