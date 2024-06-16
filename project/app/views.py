from django.shortcuts import render
from .models import Product
from .serializer import Productserializer
from rest_framework.response  import Response
from django.http import JsonResponse

# Create your views here.

def Product_view(request):
    malik=Product.objects.all()
    serializer=Productserializer(malik, many=True)
    return JsonResponse(serializer.data,safe=False)

