from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.EventoListView.as_view(), name='eventos'),
    path('evento/<int:pk>', views.EventoDetalleView.as_view(), name='evento-detalle'),
]

urlpatterns += [   
    path('evento/<int:pk>/inscribirse/', views.inscribir_evento, name='inscribir-evento'),
]