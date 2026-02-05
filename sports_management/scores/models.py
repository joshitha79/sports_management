from django.db import models
from teams.models import Team


class Score(models.Model):
    
    team=models.ForeignKey(Team,on_delete=models.CASCADE)   
    runs=models.PositiveIntegerField()
    wickets=models.PositiveIntegerField()
    overs=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.team.team_name} - {self.runs}/{self.wickets} in {self.overs} overs"
        
# Create your models here.
