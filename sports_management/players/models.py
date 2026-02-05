from django.db import models
from teams.models import Team

class Player(models.Model):
    name=models.CharField(max_length=100)
    # age=models.PositiveIntegerField()
    jersey_number=models.PositiveIntegerField()
    role=models.CharField(max_length=50)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.team.team_name})"



