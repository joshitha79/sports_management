from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    team1_name = serializers.CharField(source="team1.team_name", read_only=True)
    team2_name = serializers.CharField(source="team2.team_name", read_only=True)
    venue_name = serializers.CharField(source="venue.venue_name", read_only=True)

    class Meta:
        model = Match
        fields = "__all__"

    def validate(self, data):
        team1 = data.get("team1")
        team2 = data.get("team2")
        if team1 == team2:
            raise serializers.ValidationError("team1 and team2 cannot be same.")
        return data

