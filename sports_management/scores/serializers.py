
from rest_framework import serializers
from .models import Score

class ScoreSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.team_name", read_only=True)

    class Meta:
        model = Score
        fields = "__all__"

    def validate(self, data):
        match = data.get("match")
        team = data.get("team")

        if match and team:
            if team not in [match.team1, match.team2]:
                raise serializers.ValidationError(
                    "Score team must be either match.team1 or match.team2"
                )

        return data
