from django.db import models
from teams.models import Team
from venues.models import Venue


class Match(models.Model):
    STATUS_CHOICES = (
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )

    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team1")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team2")

    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True)
    score=models.ForeignKey("scores.Score",on_delete=models.SET_NULL,null=True,blank=True,related_name="match_score")    
    match_date = models.DateTimeField()
    match_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")

    winner_team = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True,blank=True,related_name="matches_won")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team1.team_name} vs {self.team2.team_name}"


# Create your models here.
