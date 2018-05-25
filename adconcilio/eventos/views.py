from django.shortcuts import render

# Create your views here.
from .models import Evento
from django.views import generic
from cart import *

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    
        
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        
    )

    
class EventoListView(generic.ListView):
    model = Evento
    
    

class EventoDetalleView(generic.DetailView):
    model = Evento
    
    def evento_detalle_view(request,pk):
    
        try:
            evento_id=Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            raise Http404("Evento no existe")
    
        return render(
            request,
            'eventos/evento_detalle.html',
            context={'evento':evento_id,}
        )

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Registro

class RegistroCreate(CreateView):
    model = Registro
    fields = '__all__'
    #initial={'date_of_death':'05/01/2018',}

