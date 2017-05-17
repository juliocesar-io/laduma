# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin


admin.site.register(Template)
admin.site.register(Package)
admin.site.register(Order)
admin.site.register(Client)
# Register your models here.
