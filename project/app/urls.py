from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('products/',views.Product_view),
]
