from django.contrib import admin

# Register your models here.
from .models import Evento, EventoMaterial, Promocion, FechaEvento, Exposicion, AgentePago, Localidad, Expositor, Recibo, Registro, Participante

admin.site.register(Evento)
admin.site.register(EventoMaterial)
admin.site.register(Promocion)
admin.site.register(FechaEvento)
admin.site.register(Exposicion)
admin.site.register(AgentePago)
admin.site.register(Localidad)
admin.site.register(Expositor)
admin.site.register(Recibo)
admin.site.register(Registro)
admin.site.register(Participante)
