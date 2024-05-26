from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    
    producto = Producto.objects.all()
    #Con HttpResponse es la mejor opción.
    #print(producto)
    #return HttpResponse(producto[0].nombre)

    #Con JSONResponse se usa cuando estamos a las apuradas y necesitamos ir a Producción.
    #producto = Producto.objects.all().values()
    #return JsonResponse(list(producto), safe=False)

    return render(
        request,
        'index.html',
        context={'productos':producto}
    )

def detalle(request, producto_id):

    producto = Producto.objects.get(id = producto_id)

    return render(
        request,
        'detalle.html',
        context={"producto": producto }
    )