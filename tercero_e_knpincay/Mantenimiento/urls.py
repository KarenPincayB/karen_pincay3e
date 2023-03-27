from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicioDef, name='inicio'),
    path('crearRopa/', views.crearRopaDef, name='crear'),
    path('registrarRopa/', views.registrarRopaDef, name='registrarRopa'),
    path('editarRopa/<int:id>', views.editarRopaDef, name='editarRopa'),
    path('edicionRopa/', views.edicionRopaDef, name='edicionRopa'),
    path('borrarRopa/<id>', views.borraRopaDef, name='borrarRopa'),
    path('buscar_ropa/', views.buscar_ropas, name='buscarropa'),

]