from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FunInterest(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class FunEvent(models.Model):
    name = models.CharField(max_length=200)
    Description = models.TextField(max_length=500)
    startDate = models.DateTimeField("Start Date")
    endDate = models.DateTimeField("End Date")

    def __unicode__(self):
        return self.name



