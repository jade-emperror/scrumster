from django.db import models
from datetime import datetime
class load(models.Model):
    task=models.CharField(max_length=50)
    priority=models.IntegerField()
    status=models.CharField(max_length=50)
    ticketopen=models.DateTimeField(default=datetime.now)
    ticketend=models.DateTimeField()