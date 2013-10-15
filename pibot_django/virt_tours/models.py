from django.db import models
from django.contrib.auth.models import User

class PiBotUser(models.Model):
    """
    Represents the users that are able to apply for PiBot access.
    """
    user = models.OneToOneField(User)
    joined = models.DateTimeField()

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Tour(models.Model):
    """
    Represents the current tour and the users associated with it.
    """
    date = models.DateTimeField()
    user = models.ForeignKey('PiBotUser')
    deadline = models.DateTimeField()
    pibot = models.ForeignKey('PiBot')

    def __unicode__(self):
        return (self.user.first_name + ' ' + self.user.last_name + ' | Start: ' +
    self.date + ' Deadline: ' + self.deadline + ' Using: '  + pibot)

class PiBot(models.Model):
    """
    Represents a physical PiBot that can be user controlled.
    """
    name = models.CharField(max_length=35)
    location = models.CharField(max_length=35)
    operational = models.BooleanField()
    net_address = models.IPAddressField()

    def __unicode__(self):
        return self.name + ' @ ' + self.location

       
