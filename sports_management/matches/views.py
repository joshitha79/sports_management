from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Match
from .serializers import MatchSerializer

class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all().order_by("-id")
    serializer_class = MatchSerializer


# Create your views here.
