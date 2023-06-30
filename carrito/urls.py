from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ubicacion', views.ubicacion, name='ubicacion'),
    path('contacto/', views.contacto, name= "contacto"),
    path('carrito_list/', views.carrito_list, name='carrito_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
    path('pago/', views.pago, name='pago'),
    path('registro/', views.registro, name ="registro"),
]