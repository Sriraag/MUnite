from django.db import models

# Create your models here.
class Delegate(models.Model):
  name = models.CharField(max_length=200)
  rating = models.IntegerField()
  join_date = models.DateTimeField('date joined')
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  acheivement = models.CharField(max_length=500)
  profile_pic = models.ImageField(upload_to='profile_picture/', blank=True, null=True, default='profile_picture/default-profile-picture1.jpg')

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
  description = models.CharField(max_length=2000)

  def __str__(self):
    return self.event


class Committee(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  numberOfRegistrations = models.IntegerField()
  committee_description = models.CharField(max_length=1000)
  linkToBackgroundGuide = models.URLField(max_length=200)

  def __str__(self):
    return self.name

