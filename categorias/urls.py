from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.lista_categorias, name='lista'),
    path('crear/', views.crear_categoria, name='crear'),
    path('editar/<int:id>/', views.editar_categoria, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_categoria, name='eliminar'),
]