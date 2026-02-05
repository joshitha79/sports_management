from django.db import models

class Venue(models.Model):
    venue_name=models.CharField(max_length=150)
    city=models.CharField(max_length=100)
    capacity=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.venue_name
  


