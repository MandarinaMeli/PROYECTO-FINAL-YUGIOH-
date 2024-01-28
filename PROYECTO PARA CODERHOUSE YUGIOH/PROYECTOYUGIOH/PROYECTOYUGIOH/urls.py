"""
URL configuration for PROYECTOYUGIOH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CARTAS.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("series/",ver_serie),
    path("juego/",ver_juego),
    path("pelicula/",ver_pelicula),
    path("",inicio, name="Inico"),


    #URLS CON DJANGO
    path("nuevaSerie/", agregar_serie),    
    path("nuevoJuego/", agregar_juego),
    path("nuevoPelicula/", agregar_pelicula),  


    path("listaPeli/", ListaPeliculas.as_view(), name="Lista De Peliculas"),
    path("listaSerie/", ListaSerie.as_view(),  name="Lista De Serie"),
    path("listaJuego/", ListaJuego.as_view(), name="Lista De Juego"),


    #URLS COPIA POR LAS DUDAS INTENTANDO PARA QUE SE VEA LINDO 
    #path("nuevaSerie/", SerieFormulario),    
    #path("nuevoJuego/", JuegoFormulario),
    #path("nuevoPelicula/", PeliculaFormulario),  


    #URLS CON HTML
    path("nuevaSerie/", agregar_serie_con_html),    
    path("nuevoJuego/", agregar_juego_con_html),
    path("nuevoPelicula/", agregar_pelicula_con_html),  


    #URLS BUSQUEDA
    path("buscarSerieLetra/", busqueda_serie_por_letra),
    path("resultadosSerie/", resultados_buscar_serie_año),
    path("buscarJuegoLetra/", busqueda_juego_por_letra),
    path("resultadosJuego/", resultados_buscar_juego_año),
    path("buscarPeliculaLetra/", busqueda_pelicula_por_letra),
    path("resultadosPelicula/", resultados_buscar_pelicula_año),


    #NO TOCAR
    path("nuevaSerie/", agregar_serie, name="Serie"),
    path("nuevoJuego/", agregar_juego, name="Juego"),
    path("nuevoPelicula/", agregar_pelicula, name="Pelicula"),
    path("login/", inicio_sesion, name= "Iniciar Sesión"),
    path("register/", registro, name= "Registrase"),
    path("logout/", cerrar_sesion, name="Cerrar Sesión")



]
