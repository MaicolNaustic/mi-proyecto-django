from django.shortcuts import render, redirect, get_object_or_404
from empresa.models import Empresa
from .forms import EmpresaForm
from .models import Trabajador
from .forms import TrabajadorForm
from productos.models import Producto
from .forms import ProductoForm
from proveedores.models import Proveedor
from .forms import ProveedorForm

def home(request):
    return render(request, 'core/home.html')

def nosotros(request):
    empresa = Empresa.objects.first() 
    return render(request, 'core/nosotros.html', {'empresa': empresa})

def productos(request):
    return render(request, 'core/productos.html')

def trabajadores(request):
    lista_trabajadores = Trabajador.objects.all()
    return render(request, 'core/trabajadores.html', {'trabajadores': lista_trabajadores})

def agregar_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
    else:
        form = TrabajadorForm()
    return render(request, 'core/agregar_trabajador.html', {'form': form})

def editar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, request.FILES, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'core/editar_trabajador.html', {'form': form})

def eliminar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajadores')
    return render(request, 'core/eliminar_trabajador.html', {'trabajador': trabajador})

def proveedores(request):
    return render(request, 'core/proveedores.html')

def agregar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nosotros')
    else:
        form = EmpresaForm()
    return render(request, 'core/agregar_empresa.html', {'form': form})

def editar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('nosotros')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'core/editar_empresa.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'core/agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'core/eliminar_producto.html', {'producto': producto})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'core/proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'core/agregar_proveedor.html', {'form': form})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'core/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores')
    return render(request, 'core/eliminar_proveedor.html', {'proveedor': proveedor})