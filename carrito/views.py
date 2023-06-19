from django.utils import timezone
from .models import Publicacion
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'carritos/index.html')

def carrito_list(request):
    publicacion = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'carritos/carrito_list.html', {'publicacion': publicacion})

def post_detail(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'carritos/post_detail.html', {'post': post})

