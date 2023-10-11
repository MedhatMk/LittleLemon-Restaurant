from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class MenuItems(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingList(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
