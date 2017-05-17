# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('is_deal',)
    list_display = ['id','template', 'client', 'packages_chossen', 'is_deal']

    def packages_chossen(self, obj):
     return obj.packages.all()

admin.site.register(Template)
admin.site.register(Package)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client)
# Register your models here.
