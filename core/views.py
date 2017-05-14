# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

def step_1(request):

    t = Template.objects.all()

    return render(request, 'step_1.html', {'t': t, 'step_1': True})


def step_2(request, id_template):

    t = Template.objects.get(id=id_template)
    p = t.packages.all()

    return render(request, 'step_2.html', {'t':t, 'p': p, 'step_2': True})

def step_3(request):


    return render(request, 'step_3.html', {'step_3': True})