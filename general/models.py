# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sister(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  class_year = models.IntegerField(default=0)
  PRC = models.BooleanField(default=False)
  def __str__(self):
    return self.first_name+' '+self.last_name
  # order by last name, then first
  class Meta:
    ordering = ['last_name', 'first_name']

class Setup(models.Model):
  active_setup = models.BooleanField(default=False)
  year_of_graduating_seniors = models.IntegerField(default=0)
  def __str__(self):
    return str(self.year_of_graduating_seniors-1)+'-'+str(self.year_of_graduating_seniors)