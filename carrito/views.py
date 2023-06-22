from .models import Publicacion
from django.shortcuts import render, get_object_or_404, redirect
from .forms import producto
from django.contrib import messages
def index(request):
    return render(request, 'carritos/index.html')

def pago(request):
    return render(request, 'carritos/pago.html')

def formulario(request):
    return render(request, 'carritos/formulario.html')

def ubicacion(request):
    return render(request, 'carritos/ubicacion.html')

def carrito_list(request):
    publicacion = Publicacion.objects.all()
    return render(request, 'carritos/carrito_list.html', {'publicacion': publicacion})

def post_detail(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'carritos/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = producto(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Producto registrado")
            return redirect('post_detail', pk=post.pk)
    else:
        form = producto()
    return render(request, 'carritos/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = producto(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Modificado Correctamente")
            return redirect('post_detail', pk=post.pk)
    else:
        form = producto(instance=post)
    return render(request, 'carritos/post_edit.html', {'form': form})

