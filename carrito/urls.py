from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito_list, name='carrito_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]