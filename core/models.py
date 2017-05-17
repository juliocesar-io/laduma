# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from moneyed import Money
from djmoney.models.fields import MoneyField



class Client(models.Model):
    """client info"""
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,  null=True)

    name = models.CharField(max_length=100)
    mail = models.EmailField()


    def __unicode__(self):
        return unicode(self.mail)

class Package(models.Model):
    """packages: aditional options for templates"""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=0, default_currency='MXN')


    def __unicode__(self):
        return unicode(self.name)


class Template(models.Model):
    """template: """


    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo_cover = models.FileField(upload_to='laduma/media/covers')
    url = models.URLField()
    price = MoneyField(max_digits=10, decimal_places=0, default_currency='MXN')
    packages = models.ManyToManyField(Package)

    def __unicode__(self):
        return unicode(self.title)

class Order(models.Model):
    """a client order"""
    created_date = models.DateTimeField(auto_now_add=True,  null=True)
    modified_date = models.DateTimeField(auto_now=True,  null=True)

    template = models.ForeignKey(Template)
    client = models.ForeignKey(Client)
    packages = models.ManyToManyField(Package)
    is_deal = models.BooleanField(default=False)



    def get_subtotal_amount_order(self):
        tp = self.template.price
        t = 0
        for p in self.packages.all():
            t = t + p.price
        subtotal = tp + t

        return subtotal

    def get_order_tax(self):
        t = self.get_subtotal_amount_order()
        tax = t * 0.16

        return tax


    def get_total_amount_order(self):
        t = self.get_subtotal_amount_order()
        tax = self.get_order_tax()
        total = t + tax

        return total


    def __unicode__(self):
        return unicode(self.id)



