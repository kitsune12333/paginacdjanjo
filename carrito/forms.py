from django import forms
from .models import Publicacion

class producto(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = '__all__'