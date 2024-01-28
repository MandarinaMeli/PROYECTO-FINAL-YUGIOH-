from django.shortcuts import render
from django.http import HttpResponse
from CARTAS.models import Serie , Juego , Pelicula
from CARTAS.forms import SerieFormulario, JuegoFormulario, PeliculaFormulario
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here
@login_required
def ver_serie(request):

    mis_series = Serie.objets.all()
    info = {"series":mis_series}

    return render(request, "CARTAS/series.html", info)

@login_required
def ver_juego(request):

    mis_juego = Juego.objets.all()
    info = {"series":mis_juego}

    return render(request, "CARTAS/juego.html", info)

@login_required
def ver_pelicula(request):

    mis_pelicula = Pelicula.objets.all()
    info = {"series":mis_pelicula}

    return render(request, "CARTAS/peliculas.html", info)



def inicio(request): 

    return render(request,"CARTAS/inicio.html")


def agregar_serie(request):
 
    serie1 = Serie(nombre = "YUGIOH DUEL MONSTERS", año = 2004, invocacion = "sacrificio", personajes = "Yugi Muto") #Crear un objeto usando el modulo
    serie1.save()

    return HttpResponse("Se agrego una serie..")
  


def agregar_juego(request):
    
    juego1 = Juego(nombre = "YUGIOH Duel Link", año = 2006, invocacion = "sacrificio,especial,xyz,sincro,pendulo", personajes = "Yugi Muto, Seto Kaiba") #Crear un objeto usando el modulo
    juego1.save()

    return HttpResponse("Se agrego un juego..")


def agregar_pelicula(request):
    
    pelicula1 = Pelicula(nombre = "YUGIOH ", año = 2007, invocacion = "sacrificio,especial,xyz,sincro,pendulo", personajes = "Yugi Muto, Seto Kaiba, Joy willer") #Crear un objeto usando el modulo
    pelicula1.save()

    return HttpResponse("Se agrego un juego..")







def agregar_serie(request):
 


    return render(request, "CARTAS/nuevo_serie.html")
 

def agregar_juego(request):
 


    return render(request, "CARTAS/nuevo_juego.html")


def agregar_pelicula(request):
 


    return render(request, "CARTAS/nuevo_pelicula.html")







#def agregar_serie(request):

    if request.method == "POST":

        nuevo_formulario = SerieFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            serie_nueva = Serie(nombre= info["nombre"], año= info["año"], invocacion=info["invocacion"], personajes=info["personajes"])

            serie_nueva.save()

            return render(request, "CARTAS/inicio.htlm")
    
    else:
        
        nuevo_formulario= SerieFormulario()

    return render(request, "CARTAS/formu_serie.html",{"mi_formu":nuevo_formulario})   



#def agregar_pelicula(request):

    if request.method == "POST":

        nuevo_formulario = PeliculaFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            pelicula_nueva = Pelicula(nombre= info["nombre"], año= info["año"], invocacion=info["invocacion"], personajes=info["personajes"])  

            pelicula_nueva.save()

            return render(request, "CARTAS/inicio.htlm")
    
    else:
        
        nuevo_formulario= PeliculaFormulario()        

    return render(request, "CARTAS/formu_pelicula.html", {"mi_formu":nuevo_formulario})    



#def agregar_juego(request):

    if request.method == "POST":

        nuevo_formulario = JuegoFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            juego_nueva = Juego(nombre= info["nombre"], año= info["año"], invocacion=info["invocacion"], personajes=info["personajes"])   

            juego_nueva.save()

            return render(request, "CARTAS/inicio.htlm")
    
    else:
        
        nuevo_formulario= JuegoFormulario()        

    return render(request, "CARTAS/formu_juego.html", {"mi_formu":nuevo_formulario} )    


#AGREGAR SERIE CON HTML
def agregar_serie_con_html(request):
    if request.method == "POST":
        
        serie_nueva = Serie(
            nombre = request.POST["name"],
            año = request.POST ["year"],
            invocacion = request.POST["invocation"],
            personajes = request.POST["character"],)

        serie_nueva.save()
    return render(request,"CARTAS/nuevo_serie.html")


#AGREGAR JUEGO CON HTML
def agregar_juego_con_html(request):
    if request.method == "POST":
        
        juego_nueva = Juego(
            nombre = request.POST["name"],
            año = request.POST ["year"],
            invocacion = request.POST["invocation"],
            personajes = request.POST["character"],)

        juego_nueva.save()
    return render(request,"CARTAS/nuevo_juego.html")



#AGREGAR PELICULA CON HTML
def agregar_pelicula_con_html(request):
    if request.method == "POST":
        
        pelicula_nueva = Pelicula(
            nombre = request.POST["name"],
            año = request.POST ["year"],
            invocacion = request.POST["invocation"],
            personajes = request.POST["character"],)

        pelicula_nueva.save()
    return render(request,"CARTAS/nuevo_pelicula.html")




#BUSQUEDA DE SERIE
def busqueda_serie_por_letra(request):

    return render(request, "CARTAS/buscar_serie_letra.html")


def resultados_buscar_serie_año(request):

    if request.method=="GET":
        
        año_pedido=request.GET["año"]
        resultados_series= Serie.objects.filter(año__icontains=año_pedido)

        return render(request, "CARTAS/buscar_serie_letra.html",{"series":resultados_series})
    
    else:

        return render (request, "CARTAS/buscar_serie_letra.html")




#BUSQUEDA DE JUEGO
def busqueda_juego_por_letra(request):

    return render(request, "CARTAS/buscar_juego_letra.html")


def resultados_buscar_juego_año(request):

    if request.method=="GET":
        
        año_pedido=request.GET["año"]
        resultados_juego= Juego.objects.filter(año__icontains=año_pedido)

        return render(request, "CARTAS/buscar_juego_letra.html",{"series":resultados_juego})
    
    else:

        return render (request, "CARTAS/buscar_juego_letra.html")







#BUSQUEDA DE PELICULA
def busqueda_pelicula_por_letra(request):

    return render(request, "CARTAS/buscar_pelicula_letra.html")


def resultados_buscar_pelicula_año(request):

    if request.method=="GET":
        
        año_pedido=request.GET["año"]
        resultados_pelicula= Pelicula.objects.filter(año__icontains=año_pedido)

        return render(request, "CARTAS/buscar_pelicula_letra.html",{"series":resultados_pelicula})
    
    else:

        return render (request, "CARTAS/buscar_pelicula_letra.html")




#LISTAS DE PELICULAS
class ListaPeliculas(ListView):

    model: Pelicula
    template_name = "CARTAS/lista_de_peliculas.html"


#LISTAS DE SERIE
class ListaSerie(ListView):

    model: Serie
    template_name = "CARTAS/lista_de_serie.html"


#LISTAS DE JUEGOS
class ListaJuego(ListView):

    model: Juego
    template_name = "CARTAS/lista_de_juego.html"



#Crear Peliculas 
class CrearPeliculas( CreateView):
    
    model= Pelicula
    template_name = "CARTAS/crear_peliculas.html"
    fields= ["nombre","año","invocacion","personajes"]
    success_url = "/listaPeli/"


#Actualizar Peliculas
class ActualizarPeliculas(UpdateView):
    
    model= Pelicula
    template_name = "CARTAS/crear_peliculas.html"
    fields= ["nombre","año","invocacion","personajes"]
    success_url = "/listaPeli/"



#Crear Series 
class CrearSeries( CreateView):
    
    model= Serie
    template_name = "CARTAS/crear_series.html"
    fields= ["nombre","año","invocacion","personajes"]
    success_url = "/listaSerie/"


#Actualizar Series
class ActualizarSeries(UpdateView):
    
    model= Serie
    template_name = "CARTAS/crear_series.html"
    fields= ["nombre","año","invocacion","personajes"]
    success_url = "/listaSerie/"



#Crear Juego 
class CrearJuegos( CreateView):
    
    model= Juego
    template_name = "CARTAS/crear_juegos.html"
    fields= ["nombre","año","invocacion","personajes"]
    success_url = "/listaJuego/"


#Actualizar Juego
class ActualizarJuegos(UpdateView):
    
    model= Juego
    template_name = "CARTAS/crear_juegos.html"
    fields= ["nombre","año","invocacion","personajes"]
    success_url = "/listaJuego/"



#INICIO SESION 
def inicio_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():

                info = formulario.cleaned_data

                usuario = info["username"]
                contra = info["password"]

                usuario_actual = authenticate(username=usuario, password=contra)

                if usuario_actual is not None: 
                    login(request, usuario_actual)

                    return render (request,"CARTAS/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

    else:
            
        formulario = AuthenticationForm()

    return render(request, "registro/inicio_sesion.html",{"formu": formulario})


#REGISTRO 
def registro(request):
    if request.method == "POST":
       
       formulario = UserCreationForm(request.POST)
 
       if formulario.is_valid():
           info= formulario.cleaned_data
           usuario=info ["username"]
           formulario.save()
           return render(request, "CARTAS/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
    else:   

        formulario=UserCreationForm()

    return render(request, "registro/registrar_usuario.html",{"formu":formulario})


#Cerrar Sesion 
def cerrar_sesion(request):
    logout(request)
    return render (request,"registro/cerrar_sesion.html")



#Editar Usuario NO PUDE HACERLO ME SALE ERROR ENTONCES LO DEJE ASI BORRE EL RESTO DE COSAS EN URL Y FORM PARA QUE NO MOLESTO EN EL PROYECTO

#def editar_perfil(request):

    usuario_actual = request.user

    if request.method == "POST":
       
       formulario = EditarUsuario(request.POST)
 
       if formulario.is_valid():
           
           info= formulario.cleaned_data

           usuario_actual.first_name = info ["first_name"]
           usuario_actual.last_name = info ["last_name"]
           usuario_actual.email = info ["email"]
           usuario_actual.set_password(info ["password1"])

           usuario_actual.save()

           return render(request, "CARTAS/inicio.html",)
    else:   

        formulario=EditarUsuario(initial={"first_name":usuario_actual.first_name,
                                            "last_name":usuario_actual.last_name,
                                            "email":usuario_actual.gmail})


    return render(request, "registro/editar_usuario.html",{"formu":formulario})
















