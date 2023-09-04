from django.urls import path, include
from .views import *           
from django.contrib.auth.views import LogoutView
from django import views

urlpatterns = [
    #Home page
    path('',tienda, name="home"),
     
    #URLS para el manejo de usuarios
    path('login/',login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/home.html"), name="logout" ),
    path('registro/', registrar, name="registro" ),
    path('editar_usuario/', editarUsuario, name="editarUsuario" ),
    path('agregar_avatar/', agregarAvatar, name="agregarAvatar" ),

    #URLS para el CRUD de Prenda
    path('catalogo_prendas/', PrendaList.as_view(), name="prendas"),
    path('crear_prenda/', PrendaCrear.as_view(), name="crear_prenda" ),
    path('editar_prenda/<int:pk>/', PrendaEditar.as_view(), name="editar_prenda" ),
    path('borrar_prenda/<int:pk>/', PrendaBorrar.as_view(), name="borrar_prenda" ),
    path('detalle_prenda/<int:pk>/', PrendaDetalle.as_view(), name="detalle_prenda"),

    #URLS para el CRUD de Calzado
    path('catalogo_calzado/',CalzadoList.as_view(), name="calzado"),
    path('crear_calzado/', CalzadoCrear.as_view(), name="crear_calzado" ),
    path('editar_calzado/<int:pk>/', CalzadoEditar.as_view(), name="editar_calzado" ),
    path('borrar_calzado/<int:pk>/', CalzadoBorrar.as_view(), name="borrar_calzado" ),
    path('detalle_calzado/<int:pk>/', CalzadoDetalle.as_view(), name="detalle_calzado"),        
    
    #URLS para el CRUD de Accesorios
    path('catalogo_accesorios/',AccesorioList.as_view(), name="accesorios"),
    path('crear_accesorio/', AccesorioCrear.as_view(), name="crear_accesorio" ),
    path('editar_accesorio/<int:pk>/', AccesorioEditar.as_view(), name="editar_accesorio" ),
    path('borrar_accesorio/<int:pk>/', AccesorioBorrar.as_view(), name="borrar_accesorio" ),
    path('detalle_accesorio/<int:pk>/', AccesorioDetalle.as_view(), name="detalle_accesorio"),

    #URLS para el CRUD de EventosBazaar
    path('cartelera_eventos/',EventoList.as_view(), name="eventos"),
    path('crear_evento/', EventoCrear.as_view(), name="crear_evento" ),
    path('editar_evento/<int:pk>/', EventoEditar.as_view(), name="editar_evento" ),
    path('borrar_evento/<int:pk>/', EventoBorrar.as_view(), name="borrar_evento" ), 
    
    #ULS para buscar Prenda
    path('irPrendaBuscar/', irPrendaBuscar, name="irPrendaBuscar" ),
    path('buscarPrenda/', buscarPrenda, name="buscarPrenda" ),
    
    #ULS para buscar Calzado
    path('irCalzadoBuscar/', irCalzadoBuscar, name="irCalzadoBuscar" ),
    path('buscarCalzado/', buscarCalzado, name="buscarCalzado" ),
    
    #ULS para buscar Accesorio
    path('irAccesorioBuscar/', irAccesorioBuscar, name="irAccesorioBuscar" ),
    path('buscarAccesorio/', buscarAccesorio, name="buscarAccesorio" ),
    
    #ULS para buscar EventosBazaar
    path('irEventoBuscar/', irEventoBuscar, name="irEventoBuscar" ),
    path('buscarEvento/', buscarEvento, name="buscarEvento" ),

    #URL para nostros
    path('sobre_nosotros/',nosotros, name="nosotros")
]