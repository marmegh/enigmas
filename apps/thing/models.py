# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User
import datetime

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination'])<1:
            errors['destination']= "Destination required"
        if len(postData['plan'])<1:
            errors['plan']= 'Description required'
        start = postData['start']
        end = postData['end']
        today = datetime.date.today()
        return errors

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=255)
    planner = models.ForeignKey(User, related_name = 'trips')
    plan = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    objects = TripManager()
class Join(models.Model):
    trip = models.ForeignKey(Trip, related_name = 'joins')
    joiner = models.ForeignKey(User, related_name = 'joiners', blank = True)
