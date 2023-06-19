from django import forms

from .models import Publicacion

class PostForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('title', 'price', 'descripcion',)