from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carrito_list/', views.carrito_list, name='carrito_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]