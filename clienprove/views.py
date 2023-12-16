from django.shortcuts import render, redirect
from .models import Cliente, Proveedor, Factura
from .forms import ClienteForm, ProveedorForm, FacturaForm
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Cliente
from django.http import HttpResponse  
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Factura
from .forms import FacturaForm, FacturaFormSet
from django import template




def index(request):
    
    return render(request, 'base.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'templates_base/base.html', {'clientes': clientes})


#CREAR CLIENTES Y PROVEEDORES

def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')  
    else:
        form = ClienteForm()

    return render(request, 'add_cliente.html', {'form': form})

def add_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = ProveedorForm()

    return render(request, 'add_proveedor.html', {'form': form})

#MOSTRAR

def show_clientes(request):
    clientes = Cliente.objects.all()
    factura_form = FacturaForm()  

    return render(request, 'show_clientes.html', {'clientes': clientes, 'factura_form': factura_form})

def show_proveedores(request):
    proveedores = Proveedor.objects.all()  
    return render(request, 'show_proveedores.html', {'proveedores': proveedores})



#detalles del cliente y proveedor




def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'cliente_info.html', {'cliente': cliente})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    return render(request, 'proveedor_info.html', {'proveedor': proveedor})


#facturas




def crear_factura(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        formset = FacturaFormSet(request.POST, prefix='factura')
        if formset.is_valid():
            for form in formset:
                factura = form.save(commit=False)
                factura.cliente = cliente
                factura.total = factura.cantidad * factura.precio
                factura.save()

            return redirect('mostrar_facturas', cliente_id=cliente.id)
    else:
        formset = FacturaFormSet(prefix='factura')

    return render(request, 'crear_factura.html', {'formset': formset, 'cliente': cliente})


def mostrar_facturas(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    facturas = Factura.objects.filter(cliente=cliente)

    return render(request, 'mostrar_facturas.html', {'cliente': cliente, 'facturas': facturas})
