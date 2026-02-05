from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.team_name", read_only=True)
    class Meta:
        model=Player
        fields="__all__"
