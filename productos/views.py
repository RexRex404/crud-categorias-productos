
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def lista_productos(peticion):
    productos = Producto.objects.select_related('categoria').all()
    return render(peticion, 'productos/lista.html', {'productos': productos})


def crear_producto(peticion):
    if peticion.method == 'POST':
        formulario = ProductoForm(peticion.POST, peticion.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos:lista')
    else:
        formulario = ProductoForm()
    return render(peticion, 'productos/formulario.html', {'formulario': formulario, 'titulo': 'Crear producto'})


def editar_producto(peticion, id):
    producto = get_object_or_404(Producto, id=id)
    if peticion.method == 'POST':
        formulario = ProductoForm(peticion.POST, peticion.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos:lista')
    else:
        formulario = ProductoForm(instance=producto)
    return render(peticion, 'productos/formulario.html', {'formulario': formulario, 'titulo': 'Editar producto'})


def eliminar_producto(peticion, id):
    producto = get_object_or_404(Producto, id=id)
    if peticion.method == 'POST':
        producto.delete()
        return redirect('productos:lista')
    return render(peticion, 'productos/eliminar.html', {'producto': producto})