
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm


def lista_categorias(peticion):
    categorias = Categoria.objects.all()
    return render(peticion, 'categorias/lista.html', {'categorias': categorias})


def crear_categoria(peticion):
    if peticion.method == 'POST':
        formulario = CategoriaForm(peticion.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias:lista')
    else:
        formulario = CategoriaForm()
    return render(peticion, 'categorias/formulario.html', {'formulario': formulario, 'titulo': 'Crear categoría'})


def editar_categoria(peticion, id):
    categoria = get_object_or_404(Categoria, id=id)
    if peticion.method == 'POST':
        formulario = CategoriaForm(peticion.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias:lista')
    else:
        formulario = CategoriaForm(instance=categoria)
    return render(peticion, 'categorias/formulario.html', {'formulario': formulario, 'titulo': 'Editar categoría'})


def eliminar_categoria(peticion, id):
    categoria = get_object_or_404(Categoria, id=id)
    if peticion.method == 'POST':
        categoria.delete()
        return redirect('categorias:lista')
    total_productos = categoria.producto_set.count()
    return render(peticion, 'categorias/eliminar.html', {'categoria': categoria, 'total_productos': total_productos})