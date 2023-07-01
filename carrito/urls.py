from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ubicacion', views.ubicacion, name='ubicacion'),
    path('contacto/', views.contacto, name= "contacto"),
    path('carrito_list/', views.carrito_list, name='carrito_list'),
    path('publicacion/<int:pk>/', views.publicacion_detail, name='publicacion_detail'),
    path('publicacion/new', views.publicacion_new, name='publicacion_new'),
    path('publicacion/<int:pk>/edit/', views.publicacion_edit, name='publicacion_edit'),
    path('publicacion/<int:pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('pago/', views.pago, name='pago'),
    path('registro/', views.registro, name ="registro"),
]