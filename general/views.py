# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'general/index.html', {})

def about(request):
  return render(request, 'general/about.html', {})

def history(request):
  return render(request, 'general/history.html', {})

def ex(request):
  return render(request, 'general/exec.html', {})

def house(request):
  return render(request, 'general/house.html', {})

def sisterhood(request):
  return render(request, 'general/sisterhood.html', {})

def philanthropy(request):
  return render(request, 'general/philanthropy.html', {})

def rend(request, name):
  file = 'general/'+name+'.html'
  return render(request, file, {})