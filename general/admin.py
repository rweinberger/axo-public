# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sister, Setup

# Register your models here.
admin.site.register(Sister)
admin.site.register(Setup)