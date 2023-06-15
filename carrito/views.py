from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def carrito_list(request):
    publicacion = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'carritos/carrito_list.html', {'publicacion': publicacion})