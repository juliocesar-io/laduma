# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from djmoney.models.fields import MoneyField


class client(models.Model):
    """client info"""
    name = models.CharField(max_length=100)
    mail = models.EmailField()

class package(models.Model):
    """packages: aditional options for templates"""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='MXN')


class template(models.Model):
    """template: """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo_cover = models.FileField(upload_to='covers')
    url = models.URLField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='MXN')
    packages = models.ManyToManyField(package)

class order(models.Model):
    """a client order"""
    template = models.OneToOneField(template)
    client = models.OneToOneField(client)



