from django.db import models

# Create your models here.
class Delegate(models.Model):
  name = models.CharField(max_length=200)
  rating = models.IntegerField()
  join_date = models.DateTimeField('date joined')
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  acheivement = models.CharField(max_length=500)

  def __str__(self):
    return self.name


class Event(models.Model):
  core_organizer = models.ForeignKey(Delegate, on_delete = models.CASCADE)
  id = models.AutoField(primary_key=True)
  event = models.CharField(max_length=200)
  organization = models.CharField(max_length=200)
  date = models.DateTimeField('Scheduled Date')
  venue = models.CharField(max_length=200)
  price = models.IntegerField()
  description = models.CharField(max_length = 2000)

  def __str__(self):
    return self.event
