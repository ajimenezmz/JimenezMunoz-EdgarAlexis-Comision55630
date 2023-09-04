from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from .models import *
from .forms import *

# Create your views here.
#Home Page
@login_required
def home(request):
    return render(request, "app/home.html")

#Logica que permite tomar todos los productos de la tienda y mostrarlos en la home page
@login_required
def tienda(request):
    prendas = Prenda.objects.all()
    accesorios = Accesorio.objects.all()
    calzados = Calzado.objects.all()

    contexto = {
        'prendas': prendas,
        'accesorios': accesorios,
        'calzados': calzados,
    }

    return render(request, "app/home.html", contexto)

#Manejo de sesion y registro___________
def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")
            user = authenticate(username=usuario, password = password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/static/app/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "app/home.html")    
     
        else:
            return render(request, "app/login.html", {'form': formulario})
    
    formulario= AuthenticationForm()
    return render(request, 'app/login.html', {'form':formulario})

def registrar(request):
    if request.method == "POST":
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            formulario.save()
            return render(request, "app/home.html")
    else:
        formulario = RegistroForm()      
    return render(request, "app/registro.html", {"form":formulario}) 

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = EditarUsuarioForm(request.POST)
        if formulario.is_valid():
            usuario.email = formulario.cleaned_data.get('email')
            usuario.password1 = formulario.cleaned_data.get('password1')
            usuario.password2 = formulario.cleaned_data.get('password2')
            usuario.nombre = formulario.cleaned_data.get('nombre')
            usuario.apellido = formulario.cleaned_data.get('apellido')
            usuario.save()
            return render(request,"app/home.html")
        else:
            return render(request,"app/editarUsuario.html", {'form': form, 'usuario': usuario.username})
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, "app/editarUsuario.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"app/home.html")
    else:
        form = AvatarForm()
    return render(request, "app/agregarAvatar.html", {'form': form })



#CRUD del modelo Prenda y logica para el buscador del mismo modelo________________________________________________


class PrendaList(LoginRequiredMixin, ListView):
    model = Prenda

class PrendaCrear(LoginRequiredMixin, CreateView):
    model = Prenda
    fields = ['tipoPrenda',
              'tela',
              'color',
              'talla',
              'precio',
              'cantidad',
              'descripcion',
              'telefonoVendedor',
              'emailVendedor',
              'imagenPrenda']
    success_url = reverse_lazy('prendas')

class PrendaEditar(LoginRequiredMixin, UpdateView):
    model = Prenda
    fields = ['precio',
              'cantidad',
              'descripcion',
              'telefonoVendedor',
              'emailVendedor']
    success_url = reverse_lazy('prendas')

class PrendaBorrar(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('prendas')

class PrendaDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'prenda'
    template_name = 'app/prenda_detalle.html'

@login_required
def irPrendaBuscar(request):
    return render(request, "app/prenda_buscar.html")

@login_required
def buscarPrenda(request):
    buscar = request.GET.get('buscar')
    
    if buscar:
        tipoPrenda = Prenda.objects.filter(tipoPrenda__icontains=buscar)
        contexto = {"prenda_list": tipoPrenda}
        return render(request, "app/prenda_list.html", contexto)
    
    return render(request, "app/mensaje_busqueda_vacia.html")



#CRUD del modelo Calzado y logica para el buscador del mismo modelo________________________________________________

class CalzadoList(LoginRequiredMixin, ListView):
    model = Calzado

class CalzadoCrear(LoginRequiredMixin, CreateView):
    model = Calzado
    fields = ['tipoCalzado',
              'color',
              'talla',
              'precio',
              'cantidad',
              'descripcion',
              'telefonoVendedor',
              'emailVendedor',              
              'imagenCalzado']
    success_url = reverse_lazy('calzado')

class CalzadoEditar(LoginRequiredMixin, UpdateView):
    model = Calzado
    fields = ['precio',
              'cantidad',
              'descripcion',
              'telefonoVendedor',
              'emailVendedor']
    success_url = reverse_lazy('calzado')

class CalzadoBorrar(LoginRequiredMixin, DeleteView):
    model = Calzado
    success_url = reverse_lazy('calzado')

class CalzadoDetalle(LoginRequiredMixin, DetailView):
    model = Calzado
    context_object_name = 'calzado'
    template_name = 'app/calzado_detalle.html'

@login_required
def irCalzadoBuscar(request):
    return render(request, "app/calzado_buscar.html")

@login_required
def buscarCalzado(request):
    buscar = request.GET.get('buscar')
    
    if buscar:
        tipoCalzado = Calzado.objects.filter(tipoCalzado__icontains=buscar)
        contexto = {"calzado_list": tipoCalzado}
        return render(request, "app/calzado_list.html", contexto)
    
    return render(request, "app/mensaje_busqueda_vacia.html")

#CRUD del modelo Accesorio y logica para el buscador del mismo modelo________________________________________________

class AccesorioList(LoginRequiredMixin, ListView):
    model = Accesorio

class AccesorioCrear(LoginRequiredMixin, CreateView):
    model = Accesorio
    fields = ['tipoAccesorio',
              'material',
              'precio',
              'size',
              'cantidad',
              'descripcion',
              'telefonoVendedor',
              'emailVendedor',
              'imagenAccesorio']
    success_url = reverse_lazy('accesorios')

class AccesorioEditar(LoginRequiredMixin, UpdateView):
    model = Accesorio
    fields = ['precio',
              'cantidad',
              'descripcion',
              'telefonoVendedor',
              'emailVendedor']
    success_url = reverse_lazy('accesorios')

class AccesorioBorrar(LoginRequiredMixin, DeleteView):
    model = Accesorio
    success_url = reverse_lazy('accesorios')

class AccesorioDetalle(LoginRequiredMixin, DetailView):
    model = Accesorio
    context_object_name = 'accesorio'
    template_name = 'app/accesorio_detalle.html'

@login_required
def irAccesorioBuscar(request):
    return render(request, "app/accesorio_buscar.html")

@login_required
def buscarAccesorio(request):
    buscar = request.GET.get('buscar')
    
    if buscar:
        tipoAccesorio = Accesorio.objects.filter(tipoAccesorio__icontains=buscar)
        contexto = {"accesorio_list": tipoAccesorio}
        return render(request, "app/accesorio_list.html", contexto)
    
    return render(request, "app/mensaje_busqueda_vacia.html")

#CRUD del modelo EventosBazaar y logica para el buscador del mismo modelo________________________________________________

class EventoList(LoginRequiredMixin, ListView):
    model = EventosBazaar

class EventoCrear(LoginRequiredMixin, CreateView):
    model = EventosBazaar
    fields = ['ciudad',
              'direccion',
              'fecha',
              'horario',
              'descripcion']
    success_url = reverse_lazy('eventos')

class EventoEditar(LoginRequiredMixin, UpdateView):
    model = EventosBazaar
    fields = ['direccion',
              'fecha',
              'horario',
              'descripcion']
    success_url = reverse_lazy('eventos')

class EventoBorrar(LoginRequiredMixin, DeleteView):
    model = EventosBazaar
    success_url = reverse_lazy('eventos')

@login_required
def irEventoBuscar(request):
    return render(request, "app/evento_buscar.html")

@login_required
def buscarEvento(request):
    buscar = request.GET.get('buscar')
    
    if buscar:
        ciudad = EventosBazaar.objects.filter(ciudad__icontains=buscar)
        contexto = {"eventosbazaar_list": ciudad}
        return render(request, "app/eventosbazaar_list.html", contexto)
    
    return render(request, "app/mensaje_busqueda_vacia.html")
    

#Renderizar nosotros
def nosotros(request):
    return render(request, "app/nosotros.html")
