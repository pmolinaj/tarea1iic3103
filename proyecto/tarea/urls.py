from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('temporada/<int:season>', views.temporadabb, name='temporadabb'),
     path('temporada/BCS/<int:season>', views.temporadabcs, name='temporadabcs'),
     path('episodios/<int:chapter>', views.episodios, name='episodios'),
     path('personajes/<str:personaje>', views.personajes, name='personajes')
]