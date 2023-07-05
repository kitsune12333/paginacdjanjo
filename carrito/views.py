from .models import Publicacion
from django.shortcuts import render, get_object_or_404, redirect
from .forms import producto, CustomUserCreationForm, ContactoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'carritos/index.html')
def contacto(request):
    data = {
        'form':ContactoForm()
    }
    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje recibido!! Nos contactaremos a la brevedad!!")
        else:
            data["form"] = formulario
    return render(request, 'carritos/contacto.html', data)

def pago(request):
    return render(request, 'carritos/pago.html')

def formulario(request):
    return render(request, 'carritos/formulario.html')

def ubicacion(request):
    return render(request, 'carritos/ubicacion.html')

def carrito_list(request):
    publicacion = Publicacion.objects.all()
    return render(request, 'carritos/carrito_list.html', {'publicacion': publicacion})

def publicacion_detail(request, pk):
    publi = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'carritos/publicacion_detail.html', {'publi': publi})

def publicacion_new(request):
    if request.method == "POST":
        form = producto(request.POST, files=request.FILES)
        if form.is_valid():
            publi = form.save(commit=False)
            publi.author = request.user
            publi.save()
            messages.success(request, "Producto registrado")
            return redirect('publicacion_detail', pk=publi.pk)
    else:
        form = producto()
    return render(request, 'carritos/publicacion_edit.html', {'form': form})

def publicacion_edit(request, pk):
    publi = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = producto(request.POST, instance=publi, files=request.FILES)
        if form.is_valid():
            publi = form.save(commit=False)
            publi.author = request.user
            publi.save()
            messages.success(request, "Modificado Correctamente")
            return redirect('publicacion_detail', pk=publi.pk)
    else:
        form = producto(instance=publi)
    return render(request, 'carritos/publicacion_edit.html', {'form': form})

def eliminar_publicacion(request, pk):
    producto = get_object_or_404(Publicacion, id=pk)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="carrito_list")

def borrar_todo(request):
    records = Publicacion.objects.all()
    records.delete()
    return render(request, 'carritos/carrito_list.html', {'records': records})

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado Correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

