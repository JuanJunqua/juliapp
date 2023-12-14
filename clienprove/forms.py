from django import forms
from .models import Cliente, Proveedor, Factura


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    fecha = forms.DateTimeField(label='Fecha', widget=forms.TextInput(attrs={'type': 'date'}))
    producto = forms.CharField(label='Producto', max_length=100)
    cantidad = forms.IntegerField(label='Cantidad', min_value=1)
    precio = forms.DecimalField(label='Precio', min_value=0.0)
    total = forms.DecimalField(label='Total', min_value=0.0)

    class Meta:
        model = Factura
        fields = ['fecha', 'producto', 'cantidad', 'precio', 'total']