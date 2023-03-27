from django.shortcuts import render, redirect
from .models import Ropas, Marcas
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def buscar_ropas(request):
    query = request.GET.get('q')
    ropa = Ropas.objects.filter(
        Q(modelo__icontains=query) |
        Q(descripcion__icontains=query) |
        Q(precio__icontains=query) |
        Q(marca__nombre__contains=query) |
        Q(disponibilidad__icontains=query)
    )
    return render(request, 'InicioRopas.html', {'ropa': ropa})

def inicioDef(request):
    ropa = Ropas.objects.all()
    return render(request, 'InicioRopas.html', {'ropa': ropa})

def crearRopaDef(request):
    marca = Marcas.objects.all()
    return render(request, 'GestionarRopas.html', {'marca': marca})

def registrarRopaDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    marca_id = request.POST['txtMarca']
    marca = Marcas.objects.get(id=marca_id)
    disponibilidad = request.POST['txtDisponibilidad']

    try:
        ropa = Ropas.objects.create(
            id=id, modelo=modelo,
            descripcion=descripcion,
            precio=precio,
            disponibilidad=disponibilidad,
            marca=marca)
        messages.success(request, 'Ropa Añadido Correctamente.')
        return render(request, 'GestionarRopas.html', {'mensaje_tipo': 'success', 'mensaje_texto': 'Ropa Añadido Correctamente.'})

    except:
        messages.error(request, 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.')
        return render(request, 'GestionarRopas.html', {'mensaje_tipo': 'error', 'mensaje_texto': 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.'})

def editarRopaDef(request, id):
    ropa = Ropas.objects.get(id=id)
    marca = Marcas.objects.all()
    return render(request, 'EditarRopas.html', {'ropa': ropa, 'marca': marca})

def edicionRopaDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    disponibilidad = request.POST['txtDisponibilidad']

    ropa = Ropas.objects.get(id=id)
    ropa.modelo = modelo
    ropa.descripcion = descripcion
    ropa.precio = precio
    ropa.disponibilidad = disponibilidad
    ropa.save()


    return redirect('inicio')

def borraRopaDef(request, id):
    ropa = Ropas.objects.get(id=id)
    ropa.delete()
    return redirect('inicio')