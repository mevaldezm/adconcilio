from django.db import models
from datetime import datetime
from datetime import deltatime


# Create your models here.
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
#import uuid

class Evento(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    nombre = models.CharField(max_length=80, help_text='Entre el nombre del evento')
    descripcion = models.TextField(max_length=256, help_text='Entre una descripcion breve del evento')
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.DurationField(datetime.deltatime)
    imagen = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    promo = models.ForeignKey('Promocion', on_delete=models.SET_NULL, null=True)

   class Meta:
        ordering = ["nombre"]
		
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nombre   
	


class EventoMaterial(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
	libro_estudio = models.TextField(max_length=100)
	guia_estudio =  models.TextField(max_length=100 )
	MULT_MEDIA = (
        ('d', 'DVD'),
        ('c', 'CD'),
		('u', 'USB'),
		('k', 'Disco'),
		('o', 'Otro'),        
    )
	multimedios = models.CharField(max_length=1, choices=MULT_MEDIA, blank=True, default='o' )
    

   class Meta:
        ordering = ["Evento"]
		
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.evento.nombre   

		
class Promocion(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    ciclo = models.CharField(max_length=50, help_text='Entre nombre del ciclo del evento')
    fecha_inicio = models.DateField(default=datetime.today)
    fecha_fin = models.DateField(default=datetime.today)
    fecha_cierre = models.DateField(default=datetime.today)
    
    class Meta:
        ordering = ["fecha_inicio"]
		verbose_name = "Promoci\u00F3n"
		verbose_name_plural = "Promociones"
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} ({1}) {2} {3}'.format(self.ciclo, self.fecha_inicio, self.fecha_fin, self.fecha_cierre)
        
    
class FechaEvento(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=datetime.today)
    hora_inicio = models.DurationField(datetime.deltatime)
    hora_final = models.DurationField(datetime.deltatime)
    
    class Meta:
        ordering = ["fecha"]
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} ({1} {2} (3}'.format(self.evento.nombre, self.fecha, self.hora_inicio, self.hora_final)
        
   

class Exposicion(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    expositor = models.ForeignKey('Expositor', on_delete=models.SET_NULL, null=True)
    localidad = models.ForeignKey('Localidad', on_delete=models.SET_NULL, null=True)
    cap_minima = models.IntegerField(default=0, verbose_name='Capacidad Minima' )
    cap_maxima = models.IntegerField(default=0, verbose_name='Capacidad Maxima' )
	
    class Meta:
        ordering = ["fecha_inicio"]
		verbose_name = "Exposici\u00F3n"
		verbose_name_plural = "Exposiciones"

            
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.id

class Expositor(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=256)
    correo = models.EmailField()
    fecha = models.DateField(auto_now_add=True)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    EXPO_ESTADO = (
        ('a', 'activo'),
        ('i', 'inactivo'),
        
    )
    estado = models.CharField(max_length=1, choices=EXPO_ESTADO, blank=True, default='a')

    class Meta:
        ordering = ["apellido"]
		verbose_name = "Expositor"
		verbose_name_plural = "Expositores"

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.apellido, self.nombre)
        
    
class Localidad(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    nombre = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
	direccion = models.CharField(max_length=120)
    salon = models.CharField(max_length=50)
    capacidad = models.IntegerField(default=0" )
	
    class Meta:
        ordering = ["direccion"]
		verbose_name = "Localidad"
		verbose_name_plural = "Localidades"
            
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nombre

class Participante(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=120)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
	
    class Meta:
        ordering = ["apellido"]
		
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.apellido, self.nombre)

class Registro(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    agente_pago = models.ForeignKey('AgentePago', on_delete=models.SET_NULL, null=True)
    participante  = models.ForeignKey('Participante', on_delete=models.SET_NULL, null=True)
    fecha_evento = models.ForeignKey('FechaEvento', on_delete=models.SET_NULL, null=True)
	
    class Meta:
        ordering = ['Evento', 'Participante']
		
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.evento.nombre, self.participante.nombre)
        
class AgentePago(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    correo = models.EmailField()
	
    class Meta:
        ordering = ['cedula', 'nombre']     
		
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.cedula, self.nombre)        

class Recibo(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Recibo Numero')
    agente_pago = models.ForeignKey('AgentePago', on_delete=models.SET_NULL, null=True)
    registro = models.ForeignKey('Registro', on_delete=models.SET_NULL, null=True)
    referencia = models.CharField(max_length=50)
    nota = models.TextField(max_length=256)
    fecha = models.DateField(default=datetime.today, editable=False)
    #total = Registro.objects.annotate(amount=Sum('total')).order_by('-fecha')
    total = models.DecimalField((max_digits=8, decimal_places=2))
                 
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.agente_pago.cedula, self.agente_pago.nombre)        

        
