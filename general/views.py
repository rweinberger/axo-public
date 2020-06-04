# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Sister, Setup


def index(request):
  return render(request, 'general/index.html', {})

def about(request):
  setup = Setup.objects.filter(active_setup=True)[0]
  context = {
    'pres': setup.President
  }
  template = loader.get_template('general/about.html')
  # return render(request, 'general/about.html', {})
  return HttpResponse(template.render(context, request))

def history(request):
  return render(request, 'general/history.html', {})

def ex(request):
  setup = Setup.objects.filter(active_setup=True)[0]
  ex = [
    ('VP Finance', setup.VP_Finance),
    ('VP Risk Management', setup.VP_Risk_Management),
    ('VP Ritual and Fraternity Appreciation', setup.VP_Ritual_and_Fraternity_Appreciation),
    ('VP Recruitment', setup.VP_Recruitment),
    ('VP New Member Ed', setup.VP_New_Member_Ed),
    ('VP PR and Marketing', setup.VP_PR_and_Marketing),
    ('VP Membership Programming', setup.VP_Membership_Programming),
    ('Panhellenic Delegate', setup.Panhellenic_Delegate),
    ('VP Intellectual Development', setup.VP_Intellectual_Development),
    ('VP Facility Operations', setup.VP_Facility_Operations),
    ('VP Philanthropy', setup.VP_Philanthropy),
    ('VP Recruitment Information', setup.VP_Recruitment_Information)
  ]
  context = {
    'pres': setup.President,
    'crs': setup.VP_CRS,
    'exec':ex
  }
  template = loader.get_template('general/exec.html')
  return HttpResponse(template.render(context, request))

def house(request):
  return render(request, 'general/house.html', {})

def sisterhood(request):
  return render(request, 'general/sisterhood.html', {})

def philanthropy(request):
  return render(request, 'general/philanthropy.html', {})

def recruitment(request):
  return render(request, 'general/recruitment.html', {})

def faq(request):
  return render(request, 'general/faq.html', {})

def sisters(request):
  y = Setup.objects.filter(active_setup=True)[0].year_of_graduating_seniors
  a, b, c, d = y, y+1, y+2, y+3
  seniors = Sister.objects.filter(class_year=a)
  juniors = Sister.objects.filter(class_year=b)
  sophomores = Sister.objects.filter(class_year=c)
  freshmen = Sister.objects.filter(class_year=d)
  sisters = [
    (d, freshmen),
    (c, sophomores),
    (b, juniors),
    (a, seniors),
  ]
  context = {
    'sisters':sisters
  }
  template = loader.get_template('general/sisters.html')
  return HttpResponse(template.render(context, request))

def involvement(request):
  return render(request, 'general/involvement.html', {'title': 'Involvement'})

def alumni(request):
  return render(request, 'general/alumni.html', {'title': 'Alumni'})

def outsidemit(request):
  return render(request, 'general/outsidemit.html', {'title': 'Outside MIT'})

  def blm(request):
    return render(request, 'general/blm.html', {'title': 'Black Lives Matter'})
