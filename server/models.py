from django.contrib.gis.db import models
from django.contrib.auth.models import Group, User


class Gang (models.Model):
    #TODO: add fields like points, money, etc...
    group = models.OneToOneField(Group)




class Gangster(models.Model):

    #TODO: add fields like points, money, etc...
    user = models.OneToOneField(User)



class Venue(models.Model):

    #TODO:  manage category and owning team
    name = models.CharField(max_length=100)
    geometry = models.PointField()
    objects = models.GeoManager()
    owner = models.ForeignKey('Gang')
    def __unicode__(self):
        return self.name
