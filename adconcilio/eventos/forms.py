from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class InscribaseForm(forms.Form):
    nombre_evento = forms.DateField(help_text="Entre un nombre de evento")
    nombre_participante = forms.DateField(help_text="Entre un su nombre")

    def clean_nombre_evento(self):
        evento = self.cleaned_data['nombre_evento']
        particpante = self.cleaned_data['nombre_participante']
        
        #Check date is not in past. 
        if (data is none):
            raise ValidationError(_('Evento invalido'))
        
        # Remember to always return the cleaned data.
        return evento