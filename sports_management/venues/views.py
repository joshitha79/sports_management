from django.shortcuts import render
from .models import Venue
from rest_framework import viewsets
from .serializers import VenueSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset=Venue.objects.all()
    serializer_class=VenueSerializer

# Create your views here.
