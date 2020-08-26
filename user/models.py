from django.db import models

# Create your models here.
class Delegate(models.Model):
  name = models.CharField(max_length=200)
  join_date = models.DateTimeField('date joined')
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  acheivement = models.CharField(max_length=500)


  def __str__(self):
    return self.name

  
