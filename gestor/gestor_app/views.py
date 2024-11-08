# gestor_app/views.py
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestor_app/listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestor_app/agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestor_app/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'gestor_app/eliminar_producto.html', {'producto': producto})

def home(request):
    return render(request, 'gestor_app/home.html')

