from django.shortcuts import render

# Create your views here.
from .models import Participante

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_parts=Participante.objects.all().count()
        
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_parts':num_parts},
    )