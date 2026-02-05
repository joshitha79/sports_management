from django.shortcuts import render
from .serializers import PlayerSerializer
from rest_framework import viewsets
from .models import Player

class PlayerViewSet(viewsets.ModelViewSet):
    queryset=Player.objects.all()
    serializer_class=PlayerSerializer
    
# Create your views here.
