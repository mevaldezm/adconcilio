from django.shortcuts import render

# Create your views here.
from .models import Participante

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