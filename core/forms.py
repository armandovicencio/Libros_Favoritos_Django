from django import forms
from core.models import Libro

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion']

        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


