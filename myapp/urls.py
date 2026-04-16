"""
URLs - Configuración de rutas
Sin dependencia de base de datos
"""
from django.urls import path
from . import views

urlpatterns = [
    # panel inicio
    path('', views.inicio, name='inicio'),
    # galeria
    path('plantas/', views.plantas_completas, name='plantas-completas'),
    # detalle de planta
    path('plantas/<int:id>/', views.detalle_planta, name='detalle-planta'),
]

