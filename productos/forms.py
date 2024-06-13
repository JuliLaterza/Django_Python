#Se utiliza forms.py por convención de Django
from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto

        fields = ['nombre','stock','puntaje','categoria'] #Nombre de los campos que aparezcan en el formulario
        