from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def plant_param(request):
    
    nombre= "Daniel"
    apellido= "Isea"
    
    return render(request, "plant_param.html", {"name": nombre, "sname":apellido})

def plant_hija(request):
    
    return render(request, "plant-hija1.html")