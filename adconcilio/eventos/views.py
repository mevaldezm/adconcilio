from django.shortcuts import render

# Create your views here.
from .models import Evento
from django.views import generic

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

class Item:
    'Clase base del Shopping Cart'
    precio = 0.00
    descripcion = ''
    
    
    def __init__(self, descripcion, precio):
    
        self.descripcion = descripcion
        self.precio = precio

    def getDescripcion(self):
        return self.descripcion
    
    def getPrecio(self):
        return self.precio

    def AddItem(self, item):
        return
        
    def RemoveItem(self, item):
        return
        
    def getItems(self):
       return
    
    def __str__(self):
        return '{0},... {1:.2f}'.format(self.descripcion, self.getPrecio())
    

class Part(Item):

    'Entry unitario'
              
    def getItems(self):
        return [0]
   
   
class Bundle(Item):
    
    __items = []

    def __init__(self, descripcion):
    
        Item.descripcion = descripcion
        Item.precio = 0.0
        
    def AddItem(self, item):
        self.__items.append(item)

    def RemoveItem(self, item):
        self.__items.remove(item) 

    def getItems(self):
        return self.__items

    def getPrecio(self):
        total = 0.0
        for item in self.__items:
            total += item.precio
        return total
    
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



from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


from .forms import InscribaseForm


def inscribir_evento(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    evento_inst=get_object_or_404(Evento, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = InscribaseForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'eventos/inscribirse_evento.html', {'form': form, 'eventoinst':evento_inst})
  