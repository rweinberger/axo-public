# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sister(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  class_year = models.IntegerField(default=0)
  PRC = models.BooleanField(default=False)
  class Meta:
    #ordered by last name, then first
    ordering = ['last_name', 'first_name']
  def __str__(self):
    return self.first_name+' '+self.last_name