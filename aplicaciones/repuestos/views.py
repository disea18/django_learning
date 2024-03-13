from django.shortcuts import render
from aplicaciones.repuestos.models import Repuestos



# Create your views here.

def repuestos(request):

    var1 = Repuestos.objects.all()  
    return render(request, "repuestos.html", {'rep':var1})