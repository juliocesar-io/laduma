# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('is_deal',)
    list_display = ['id','template', 'client', 'packages_chossen', 'is_deal']

    def packages_chossen(self, obj):
     return obj.packages.all()

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'mail']


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'photo_cover', 'url', 'get_packages', 'price']

    def get_packages(self, obj):
     return obj.packages.all()


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name','description', 'price']


admin.site.register(Template, TemplateAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
# Register your models here.
