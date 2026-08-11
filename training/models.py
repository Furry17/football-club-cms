from django.db import models


class Training(models.Model):
    training_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return (
            f"{self.training_date.strftime('%d.%m.%Y')} "
            f"{self.start_time.strftime('%H:%M')} - "
            f"{self.location}"
        )