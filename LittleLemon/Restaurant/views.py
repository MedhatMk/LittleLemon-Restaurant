from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
# Create your views here.

class MenuItems(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer