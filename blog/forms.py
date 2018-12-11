from django import forms
from .models import Tienda, Region, Ciudad,Producto,Lista
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
User = get_user_model()
class TiendaForm(forms.ModelForm):

    class Meta:
        model = Tienda
        fields = ('nombre','sucursal','direccion','region','ciudad')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()

        if 'region' in self.data:
                try:
                    region_id = int(self.data.get('region'))
                    self.fields['ciudad'].queryset = Ciudad.objects.filter(region_id=region_id).order_by('nombre')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty Ciudad queryset
        elif self.instance.pk:
            self.fields['ciudad'].queryset = self.instance.region.ciudad_set.order_by('nombre')
            

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        
        fields = ['nombre']

    
    def __init__(self, *args, **kwargs):
        super(ListaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class ProductoForm(forms.ModelForm):


    class Meta:
        model = Producto
        fields = ['nombre','costoPresupuestado','costoReal','notasAdicionales', 'estado','tienda','lista']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','costoPresupuestado','costoReal','notasAdicionales', 'estado','tienda']

    def __init__(self, *args, **kwargs):
        super(DetalleProductoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            instance = getattr(self, 'nombre', '')
            if instance is not None:
                self.fields['nombre'].widget.attrs['readonly'] = True
                self.fields['costoPresupuestado'].widget.attrs['readonly'] = True
                self.fields['notasAdicionales'].widget.attrs['readonly'] = True
                self.fields['tienda'].widget.attrs['disabled'] = True
                
    def clean_nombre(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.nombre
        else:
            return self.cleaned_data['nombre']
 
  
        
        
DetalleCompraFormSet = inlineformset_factory(Lista, Producto, form=ProductoForm, extra=5)


DetalleCompraFormSetV2 = inlineformset_factory(Lista, Producto, form=DetalleProductoForm, extra=10)



    


  
   


  






