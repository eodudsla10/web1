from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index),
    path('products.html', views.products),
    path('about.html', views.about),
    path('contact.html', views.contact, name="contact"),
    path('single-product.html', views.single_product),
    path('single-product2.html', views.single_product2),
    path('single-product3.html', views.single_product3),
    path('single-product4.html', views.single_product4),
    path('createshop/',views.createshop, name="createshop" ),
]
