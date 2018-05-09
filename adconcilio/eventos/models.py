from django.db import models
from datetime import datetime
from datetime import deltatime
from datetime import time

# Create your models here.
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
#import uuid

class Evento(models.Model):

    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=256)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.TimeField(default=datetime.now().replace(hour=4, minute=0, second=0, microsecond=0), blank=True)
	#fecha_efectiva = models.DateField(default=datetime.datetime.strptime("9999-31-12", "%Y-%m-%d").date())
	fecha_efectiva = models.DateField(default=datetime.datetime.date(9999, 12, 31))
	EVENT_ESTADO = (
        ('a', 'activo'),
        ('i', 'inactivo'),
    )
	models.CharField(max_length=1, choices=EVENT_ESTADO, blank=True, default='a' )
       
    class Meta:
        ordering = ["nombre"]
		
    def __str__(self):

        return self.nombre   
	
class Material(models.Model):

    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
	libro_estudio = models.TextField(max_length=80)
	guia_estudio =  models.TextField(max_length=80)
	MULT_MEDIA = (
        ('d', 'DVD'),
        ('c', 'CD'),
		('u', 'USB'),
		('k', 'Disco'),
		('o', 'Otro'),        
    )
	multi_medios = models.CharField(max_length=1, choices=MULT_MEDIA, blank=True, default='o' )
 
   class Meta:
        ordering = ["Evento"]
		verbose_name="Material"
		verbose_name_plural="Materiales"
		
    def __str__(self):

        return self.evento.nombre   

		
class Promocion(models.Model):

    nombre_ciclo = models.ForeignKey('Ciclo', on_delete=models.SET_NULL, null=True)
	nombre_programa = models.ForeignKey('Programa', on_delete=models.SET_NULL, null=True)
	evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    fecha_inicio = models.DateField(default=datetime.today)
    fecha_fin = models.DateField(default=datetime.today + timedelta(days=30))
    imagen = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    class Meta:
        ordering = ["fecha_inicio"]
		verbose_name = "Promoci\u00F3n"
		verbose_name_plural = "Promociones"
        
    def __str__(self):
    
        return self.evento.nombre
        
class Ciclo(models.Model):
        
    nombre = models.CharField(max_length=80)
        
    def __str__(self):
    
        return self.nombre
        
        
class Programa(models.Model):
        
    nombre = models.CharField(max_length=80)
        
    def __str__(self):
    
        return self.evento.nombre
        
  
class Exposicion(models.Model):
    
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    expositor = models.ForeignKey('Expositor', on_delete=models.SET_NULL, null=True)
    localidad = models.ForeignKey('Localidad', on_delete=models.SET_NULL, null=True)
    fecha_inicio = models.DateField(default=datetime.today, blank=True)
    hora_inicio = models.TimeField(default=time(10, 0, 0, 0), blank=True)
    hora_final = models.TimeField(default=time(12, 0, 0, 0), blank=True)
	
    class Meta:
        ordering = ["fecha_inicio"]
		verbose_name = "Exposici\u00F3n"
		verbose_name_plural = "Exposiciones"

            
    def __str__(self):
    
        return evento.nombre

class Expositor(models.Model):
    
    cedula = models.CharField(max_length=11)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=256)
    correo = models.EmailField()
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    EXPO_ESTADO = (
        ('a', 'activo'),
        ('i', 'inactivo'),
        
    )
    estado = models.CharField(max_length=1, choices=EXPO_ESTADO, blank=True, default='a')
    fecha = fecha = models.DateField(default=datetime.today, editable=False)
	
    class Meta:
        ordering = ["apellido", "nombre"]
		verbose_name = "Expositor"
		verbose_name_plural = "Expositores"

    def __str__(self):
    
        return '{0}, {1}'.format(self.apellido, self.nombre)
        
    
class Localidad(models.Model):
        
    nombre = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
	direccion = models.CharField(max_length=120)
    salon = models.CharField(max_length=50)
    capacidad = models.IntegerField(default=0 )
	
    class Meta:
        ordering = ["direccion"]
		verbose_name = "Localidad"
		verbose_name_plural = "Localidades"
            
    def __str__(self):
    
        return self.nombre

class Participante(models.Model):
    
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=120)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
	fecha = models.DateField(default=datetime.today, editable=False)
	
    class Meta:
        ordering = ["apellido", "nombre"]
		
    def __str__(self):
    
        return '{0}, {1}'.format(self.apellido, self.nombre)

class Registro(models.Model):
      
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
	exposicion = models.ForeignKey('Exposicion', on_delete=models.SET_NULL, null=True)
    participante  = models.ForeignKey('Participante', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=datetime.today, editable=False)
    class Meta:
        ordering = ['Evento', 'Participante']
		
    def __str__(self):
    
        return '{0}, {1}'.format(self.evento.nombre, self.participante.nombre)
        

class Recibo(models.Model):
       
    registro = models.ForeignKey('Registro', on_delete=models.SET_NULL, null=True)
    referencia = models.CharField(max_length=50)
    nota = models.TextField(max_length=256)
    fecha = models.DateField(default=datetime.today, editable=False)
    #total = Registro.objects.annotate(amount=Sum('total')).order_by('-fecha')
    total = models.DecimalField((max_digits=8, decimal_places=2))
                 
    def __str__(self):
        return '{0}, {1}'.format(self.registro.participante.cedula, self.registro.participante.nombre)        

        
