# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Sister, Setup


def index(request):
  return render(request, 'general/index.html', {})

def about(request):
  return render(request, 'general/about.html', {})

def history(request):
  return render(request, 'general/history.html', {})

def ex(request):
  return render(request, 'general/exec.html', {})

def house(request):
  return render(request, 'general/construction.html', {'title': 'Our House'})

def sisterhood(request):
  return render(request, 'general/sisterhood.html', {})

def philanthropy(request):
  return render(request, 'general/construction.html', {'title': 'Philanthropy'})

def recruitment(request):
  return render(request, 'general/recruitment.html', {})

def faq(request):
  return render(request, 'general/faq.html', {})

def sisters(request):
  y = Setup.objects.get(active_setup=True).year_of_graduating_seniors
  a, b, c, d = y, y+1, y+2, y+3
  seniors = Sister.objects.filter(class_year=a)
  juniors = Sister.objects.filter(class_year=b)
  sophomores = Sister.objects.filter(class_year=c)
  freshmen = Sister.objects.filter(class_year=d)
  sisters = [
    (a, seniors),
    (b, juniors),
    (c, sophomores),
    (d, freshmen)
  ]
  context = {
    'sisters':sisters
  }
  template = loader.get_template('general/sisters.html')
  return HttpResponse(template.render(context, request))

def involvement(request):
  return render(request, 'general/involvement.html', {})