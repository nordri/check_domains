from django.db import models

# Create your models here.
class Domain(models.Model):
  name = models.CharField(max_length=100)
  days = models.DateField()

  def __str__(self):
    return self.name

  def __unicode__(self):
    return self.name

class Filter(models.Model):
  filterByDays = models.IntegerField()
  
