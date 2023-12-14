from django.shortcuts import render, redirect
from .models import Cliente, Proveedor, Factura
from .forms import ClienteForm, ProveedorForm, FacturaForm
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Cliente
from django.http import HttpResponse  




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
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save(commit=False)
            factura.cliente = cliente
            factura.save()

           

            
            
            return redirect('mostrar_facturas', cliente_id=cliente.id)
        
            
    else:
        form = FacturaForm()

    return render(request, 'crear_factura.html', {'form': form, 'cliente': cliente})


def mostrar_facturas(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    facturas = Factura.objects.filter(cliente=cliente)

    return render(request, 'mostrar_facturas.html', {'cliente': cliente, 'facturas': facturas})


