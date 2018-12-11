from django.shortcuts import render,redirect,get_object_or_404
from .models import Ciudad,Region,Producto,Tienda,Lista
from .forms import TiendaForm,ProductoForm,ListaForm, DetalleCompraFormSet,DetalleCompraFormSetV2
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Sum,Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()


# Create your views here.

def main(request):
    return render(request, 'blog/index.html')
    

def registro(request):
    tienda = TiendaForm()
    return render(request, 'blog/registro.html',{'tienda':tienda})

def registro(request):
    if request.method == "POST":
        tienda = TiendaForm(request.POST)
        if tienda.is_valid():
            tienda = tienda.save(commit=False)
            tienda.save()
            return redirect('blog:home')
    else:
        tienda = TiendaForm()
    return render(request, 'blog/Registro.html', {'tienda': tienda})


def load_ciudades(request):
    region_id = request.GET.get('region')
    ciudades = Ciudad.objects.filter(region_id=region_id).order_by('nombre')
    return render(request, 'blog/ciudad_dropdown_list_options.html', {'ciudades': ciudades})

def producto(request):
    producto = ProductoForm()
    return render(request,'blog/producto.html',{'producto':producto})


def producto(request):
    if request.method == "POST":
        producto = ProductoForm(request.POST)
        if producto.is_valid():
            producto = producto.save(commit=False)
            producto.save()
            return redirect('blog:home')
    else:
        producto = ProductoForm()
    return render(request, 'blog/producto.html', {'producto':producto})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'blog/compras_detail.html', {'productos': producto})



class ListadoCompras(ListView):
    model = Lista
    template_name = 'blog/compras_list.html'
    context_object_name = 'compras'

class CrearCompra(CreateView):
    model = Lista
    
    template_name = 'blog/lista_add.html'
    form_class = ListaForm
  
    success_url = reverse_lazy('blog:compras_list')
    
    def get(self, request, *args, **kwargs):
        """Primero ponemos nuestro object como nulo, se debe tener en
        cuenta que object se usa en la clase CreateView para crear el objeto"""
        self.object = None
        #Instanciamos el formulario de la Compra que declaramos en la variable form_class
        form_class = self.get_form_class()
        form = self.get_form(form_class)
     
        
        #Instanciamos el formset
        detalle_orden_compra_formset=DetalleCompraFormSet()
        #Renderizamos el formulario de la compra y el formset
        return self.render_to_response(self.get_context_data(form=form ,detalle_compra_form_set=detalle_orden_compra_formset))

    def post(self, request, *args, **kwargs):
        #Obtenemos nuevamente la instancia del formulario de Compras
        form_class = self.get_form_class()
        form = self.get_form(form_class)
      
        
        #Obtenemos el formset pero ya con lo que se le pasa en el POST
        detalle_compra_form_set = DetalleCompraFormSet(request.POST)
        """Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
        form_valid o en caso contrario se llama al método form_invalid"""
        if form.is_valid() and detalle_compra_form_set.is_valid():
            user= form.save(commit=False)
            value = User.objects.get(username=request.user)
            user.author = value
            user.save()
            return self.form_valid(form, detalle_compra_form_set)
        else:
            return self.form_invalid(form, detalle_compra_form_set)

        
    def form_valid(self, form, detalle_compra_form_set):
        #Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
        
        
        self.object = form.save()   
        
        #Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
        detalle_compra_form_set.instance = self.object
        
        #Finalmente guardamos el formset para que tome los valores que tiene
        detalle_compra_form_set.save()
        #Redireccionamos a la ventana del listado de compras
        return HttpResponseRedirect(self.success_url)


    def form_invalid(self, form, detalle_compra_form_set):
        #Si es inválido el form de Compra o el formset renderizamos los errores
        return self.render_to_response(self.get_context_data(form=form,detalle_compra_form_set = detalle_compra_form_set))


class ModificarCompra(UpdateView):
    model = Lista
    template_name = 'blog/lista_add.html'
    form_class = ListaForm
    success_url = reverse_lazy('blog:compras_list')

    def get(self, request, *args, **kwargs):
        #Obtenemos el objeto Compra
        self.object = self.get_object()
        #Obtenemos el formulario
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #Obtenemos los detalles de la compra
        detalles = Producto.objects.filter(lista=self.object).order_by('pk')
        detalles_data = []
        #Guardamos los detalles en un diccionario
        for detalle in detalles:
            d = {'nombre': detalle.nombre,
                'costoPresupuestado': detalle.costoPresupuestado,
                'costoReal': detalle.costoReal,
                'notasAdicionales': detalle.notasAdicionales,
                'estado': detalle.estado,
                'tienda': detalle.tienda,
                }
            detalles_data.append(d)
          
        #Ponemos como datos iniciales del formset el diccionario que hemos obtenido
        
        detalle_compra_form_set = DetalleCompraFormSetV2(initial=detalles_data)
        
         #Renderizamos el formulario y el formset
        return self.render_to_response(self.get_context_data(form=form,
                                                         detalle_compra_form_set=detalle_compra_form_set))


    def post(self, request, *args, **kwargs):
    #Obtenemos el objeto compra
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_compra_form_set = DetalleCompraFormSetV2(request.POST)
        #Verificamos que los formularios sean validos
        if form.is_valid() and detalle_compra_form_set.is_valid():
            return self.form_valid(form, detalle_compra_form_set)
        else:
            return self.form_invalid(form, detalle_compra_form_set)


    def form_valid(self, form, detalle_compra_form_set):
        #Guardamos el objeto compra
        self.object = form.save()
  
        detalle_compra_form_set.instance = self.object
        #Eliminamos todas los detalles de la compra
        Producto.objects.filter(lista = self.object).delete()
        #Guardamos los nuevos detalles de la compra
        detalle_compra_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_compra_form_set):
        #Renderizamos los errores
        return self.render_to_response(self.get_context_data(form=form,
                                                         detalle_compra_form_set = detalle_compra_form_set))


def base_layout(request):
	template='blog/base.html'
	return render(request,template)

# OneSignal Register

@login_required
def onesignal_register(request):
  '''Receives the onesignal playerid of this user'''
  profile = Profile.objects.get(user=request.user) # The model where you will to save the profile.
  if request.POST.get('playerId'):
      profile.onesignal_playerId = request.POST.get('playerId')
      profile.save()
      return HttpResponse('Done')
  return HttpResponse('Something went wrong')



 


    







    








                                                       


  

    



