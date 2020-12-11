from django.db import models
import datetime

# Create your models here.

class Entry(models.Model):
    isEntry = models.BooleanField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.isEnter:
            return "Customer entered at " + self.time.date() + "."
        else:
            return "Customer exited at " + self.time.date() + "."
