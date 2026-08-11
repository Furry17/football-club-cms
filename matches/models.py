from django.db import models


class Match(models.Model):
    match_date = models.DateTimeField()
    opponent = models.CharField(max_length=100)
    is_home = models.BooleanField()
    location = models.CharField(max_length=100)
    goals_for = models.PositiveIntegerField(null=True, blank=True)
    goals_against = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        if self.is_home:
            return f"Tornádo Hradiště vs {self.opponent} on {self.match_date.strftime('%d.%m.%Y %H:%M')}"
        return f"{self.opponent} vs Tornádo Hradiště on {self.match_date.strftime('%d.%m.%Y %H:%M')}"