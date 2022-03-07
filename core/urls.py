from django.urls import path
from core.views.libros import LibrosView, LibrosDetailView
from .views.index import index

urlpatterns = [
    path('', index, name="index"),

   
    path('libros/', LibrosView.as_view(), name='libros' ),
    path('libros/<int:id>/', LibrosDetailView.as_view(), name='libros_editar' ),
]

