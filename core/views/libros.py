

from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from acceso.models import Usuario
from core.models import Libro
from core.forms import LibroForm

class LibrosView(View):
    
    def get(self, request):
        contexto = {
            'form': LibroForm(), 
            'libros' : Libro.objects.all(),
        }
        return render(request, 'core/libros.html', contexto)

    def post(self, request):
        print(request.POST)
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro Creado')
            return redirect(reverse('libros'))
        else:
            contexto = {
                'form': form, 
                'libros' : Libro.objects.all(),
            }
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/libros.html', contexto) 

class LibrosDetailView(View):
    
    def get(self, request, id):
        usuario = Libro.objects.get(id=id)
        contexto = {
            'form': LibroForm(instance=usuario), 
            'libros' : Libro.objects.all(),
        }
        return render(request, 'core/libros.html', contexto)

    def post(self, request, id):
        
        usuario = Libro.objects.get(id=id)

        form = LibroForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro Editado')
            return redirect(reverse('libros'))
        else:

            contexto = {
                'form': form, 
                'libros' : Libro.objects.all(),
            }

            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/libros.html', contexto) 