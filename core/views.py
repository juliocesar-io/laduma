# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

def index(request):

    t = Template.objects.all()

    return render(request, 'index.html', {'t': t})
