from django.contrib import admin

# Register your models here.
from .models import Evento, Material, Promocion, Exposicion, Localidad, Expositor, Registro, Participante

admin.site.register(Evento)
admin.site.register(Material)
admin.site.register(Promocion)
admin.site.register(Exposicion)
admin.site.register(Localidad)
admin.site.register(Expositor)
admin.site.register(Registro)
admin.site.register(Participante)
