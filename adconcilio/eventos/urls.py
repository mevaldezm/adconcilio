from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuestros-eventos/', views.EventoList.as_view(), name='nuestros-eventos'),
    path('nuestros-eventos/<int:pk>', views.EventoDetalleView.as_view(), name='evento-detalle'),
]