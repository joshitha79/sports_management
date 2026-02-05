from django.db import models
class Team(models.Model):
    team_name=models.CharField(max_length=150,unique=True)
    coach_name=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=55,null=True)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name


