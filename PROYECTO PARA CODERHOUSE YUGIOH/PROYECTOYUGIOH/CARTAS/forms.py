from django import forms


class SerieFormulario(forms.Form):
    nombre = forms.CharField()
    años = forms.IntegerField()
    invocacion = forms.CharField()
    personajes = forms.CharField()    

class JuegoFormulario(forms.Form):
    nombre = forms.CharField()
    años = forms.IntegerField()
    invocacion = forms.CharField()
    personajes = forms.CharField()    


class PeliculaFormulario(forms.Form):
    nombre = forms.CharField()
    años = forms.IntegerField()
    invocacion = forms.CharField()
    personajes = forms.CharField()        

