from django.utils import timezone
from .models import Publicacion
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

def index(request):
    return render(request, 'carritos/index.html')

def pago(request):
    return render(request, 'carritos/pago.html')

def formulario(request):
    return render(request, 'carritos/formulario.html')

def ubicacion(request):
    return render(request, 'carritos/ubicacion.html')

def carrito_list(request):
    publicacion = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'carritos/carrito_list.html', {'publicacion': publicacion})

def post_detail(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'carritos/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'carritos/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'carritos/post_edit.html', {'form': form})

