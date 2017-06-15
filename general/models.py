# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sister(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  class_year = models.IntegerField()
  image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
  image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
  profile_image = models.ImageField(height_field='image_height', width_field='image_width', upload_to='images', default='images/default.png', blank=True, null=True)
  PRC = models.BooleanField(default=False)
  def __str__(self):
    return self.first_name+' '+self.last_name
  class Meta:
    ordering = ['last_name', 'first_name']

class Setup(models.Model):
  active_setup = models.BooleanField(default=False)
  year_of_graduating_seniors = models.IntegerField()
  President = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='President', blank=True, null=True)
  VP_CRS = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_CRS', blank=True, null=True)
  VP_Finance = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Finance', blank=True, null=True)
  VP_Risk_Management = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Risk_Management', blank=True, null=True)
  VP_Ritual_and_Fraternity_Appreciation = models.ForeignKey(Sister, related_name='VP_Ritual_and_Fraternity_Appreciation', on_delete=models.CASCADE, blank=True, null=True)
  VP_Recruitment = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Recruitment', blank=True, null=True)
  VP_New_Member_Ed = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_New_Member_Ed', blank=True, null=True)
  VP_PR_and_Marketing = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_PR_and_Marketing', blank=True, null=True)
  VP_Membership_Programming = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Membership_Programming', blank=True, null=True)
  Panhellenic_Delegate = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='Panhellenic_Delegate', blank=True, null=True)
  VP_Intellectual_Development = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Intellectual_Development', blank=True, null=True)
  VP_Facility_Operations = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Facility_Operations', blank=True, null=True)
  VP_Philanthropy = models.ForeignKey(Sister, on_delete=models.CASCADE, related_name='VP_Philanthropy', blank=True, null=True)
  def __str__(self):
    return str(self.year_of_graduating_seniors-1)+'-'+str(self.year_of_graduating_seniors)
  class Meta:
    ordering = ['-year_of_graduating_seniors']

# class Exec_member(models.Model):
#   exec_choices = (
#     ('default', '--'),
#     ('1', 'President'),
#     ('2', 'VP CRS'),
#     ('3', 'VP Finance'),
#     ('4', 'VP Risk Management'),
#     ('5', 'VP Ritual and Fraternity Appreciation'),
#     ('6', 'VP Recruitment'),
#     ('7', 'VP New Member Ed'),
#     ('8', 'VP PR and Marketing'),
#     ('9', 'VP Membership Programming'),
#     ('10', 'Panhellenic Delegate'),
#     ('11', 'VP Intellectual Development'),
#     ('12', 'VP Facility Operations'),
#     ('13', 'VP Philanthropy'),
#     )
#   Exec_Position = models.CharField(max_length=10, choices=exec_choices, default='default')
#   sister = models.ForeignKey(Sister, on_delete=models.CASCADE)



