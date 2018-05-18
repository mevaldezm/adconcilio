from django.db import models

# Create your models here.
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
#import uuid
from datetime import datetime
from datetime import timedelta
from datetime import time
from django.core.validators import RegexValidator

class Evento(models.Model):

    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=256)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField(default=datetime.today)
    fecha_fin = models.DateField(default=datetime.today)
    duracion = models.TimeField(default=datetime.now().replace(hour=4, minute=0, second=0, microsecond=0), blank=True)
    #fecha_efectiva = models.DateField(default=datetime.strptime("9999-12-31", "%Y-%m-%d").date())
    imagen = models.ImageField(upload_to = 'event_images/', default = 'event_images/None/no-img.jpg')
    nota = models.CharField(max_length = 60, blank=True, help_text = 'Entre una nota breve')
    fecha_efectiva = models.DateField(default=datetime(9999, 12, 31), editable=False)
    EVENT_ESTADO = (
        ('a', 'activo'),
        ('i', 'inactivo'),
    )
    estado = models.CharField(max_length=1, choices=EVENT_ESTADO, blank=True, default='a' )
	
    class Meta:
        ordering = ["nombre"]
        
    def get_absolute_url(self):
        return reverse('evento-detalle', args=[str(self.id)])
        
    def __str__(self):

        return self.nombre   
    
class Material(models.Model):

    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    libro_estudio = models.CharField(max_length=80)
    guia_estudio =  models.CharField(max_length=80)
    MULT_MEDIA = (
        ('d', 'DVD'),
        ('c', 'CD'),
        ('u', 'USB'),
        ('k', 'Disco'),
        ('o', 'Otro'),        
    )
    multi_medios = models.CharField(max_length=1, choices=MULT_MEDIA, blank=True, default='o' )
 
    class Meta:
        ordering = ["evento"]
        verbose_name="Material"
        verbose_name_plural="Materiales"
        
    def __str__(self):

        return self.evento.nombre   

        
class Promocion(models.Model):

    nombre_ciclo = models.ForeignKey('Ciclo', on_delete=models.SET_NULL, null=True)
    nombre_programa = models.ForeignKey('Programa', on_delete=models.SET_NULL, null=True)
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    fecha_inicio = models.DateField(default=datetime.today)
    fecha_fin = models.DateField(default = datetime.today)
    imagen = models.ImageField(upload_to = 'promo_images/', default = 'promo_images/None/no-img.jpg')

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
    
        return self.nombre
        
  
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
    
        return self.evento.nombre

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
        ordering = ["nombre", "direccion"]
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"
            
    def __str__(self):
    
        return '{0}, {1}'.format(self.nombre, self.direccion)

class Participante(models.Model):

    numeric = RegexValidator(r'^[0-9]*$', 'Solo numeros son permitidos')
    cedula = models.CharField(max_length=11, blank=True, null=True, validators=[numeric])
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
        ordering = ['evento', 'participante']
        
    def __str__(self):
    
        return '{0}; {1}, {2} '.format(self.evento.nombre, self.participante.apellido, self.participante.nombre)
        
'''
class Factura(models.Model):
       
    participante = models.ForeignKey('Participante', on_delete=models.SET_NULL, null=True)
    referencia = models.CharField(max_length=50)
    nota = models.TextField(max_length=256)
    FACT_ESTADO = (
        ('p', 'pagada'),
        ('n', 'nueva'),
        ('c', 'cancelada'),
    )
    estado = models.CharField(max_length=1, choices=FACT_ESTADO, blank=True, default='n')
    fecha = fecha = models.DateField(default=datetime.today, editable=False)
                     
    def __str__(self):
        return '{0}, {1}'.format(self.registro.participante.cedula, self.registro.participante.nombre)        
        
class DetalleFactura(models.Model):
       
    factura = models.ForeignKey('Factura', on_delete=models.SET_NULL, null=True)
    registro = models.ForeignKey('Registro', on_delete=models.SET_NULL, null=True)
    referencia = models.CharField(max_length=50)
    nota = models.TextField(max_length=256)
    fecha = models.DateField(default=datetime.today, editable=False)
    #total = Registro.objects.annotate(amount=Sum('total')).order_by('-fecha')
    total = models.DecimalField((max_digits=8, decimal_places=2))
                 
    def __str__(self):
        return '{0}, {1}'.format(self.registro.participante.cedula, self.registro.participante.nombre)        
        
class Recibo(models.Model):
       
    Factura= models.ForeignKey('Factura', on_delete=models.SET_NULL, null=True)
    referencia = models.CharField(max_length=50)
    nota = models.TextField(max_length=256)
    fecha = models.DateField(default=datetime.today, editable=False)
    total = models.DecimalField((max_digits=8, decimal_places=2))
                 
    def __str__(self):
        return '{0}, {1}'.format(self.registro.participante.cedula, self.registro.participante.nombre)        

  '''      
