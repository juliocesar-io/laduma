# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from .forms import Step1Form, Step2Form
from formtools.wizard.views import  CookieWizardView
from django.forms.models import construct_instance
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin

FORMS = [("step1", Step1Form),
         ("step2", Step2Form)]

TEMPLATES = {"step1": "step_2.html",
             "step2": "step_3.html"}

def index(request):

    t = Template.objects.all()

    reponse = render(request, 'step_1.html', {'t': t, 'step_1': True})

    if not request.COOKIES.get('currency'):
        reponse.set_cookie('currency', 'MXN' )

    return reponse


class OrderSteps(CookieWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super(OrderSteps, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'step1':

            print context

            template_id = self.args[0]
            t = Template.objects.get(id=template_id)
            p = t.packages.all()

            context.update({'t': t, 'p': p, 'step_2': True})
        elif  self.steps.current == 'step2':

            context.update({'step_3': True})
        return context

    def get_form_initial(self, step):
        template_id = self.args[0]
        initial = self.initial_dict.get(step, {})
        initial.update({'template': template_id})
        return initial

    def done(self, form_list, form_dict, **kwargs):

        client = Client()
        form_client_step_2 = form_dict['step2']
        client = construct_instance(form_client_step_2, client, form_client_step_2.fields)
        client.save()

        new = Order()
        template_options = form_dict['step1']

        new = construct_instance(template_options, new, template_options.fields)
        new.client = Client.objects.get(id=client.pk)

        new.save()

        for i in template_options.cleaned_data['packages']:
            new.packages.add(i)
        m = client.mail

        return render(self.request, 'step_final.html', {'mail':m})

order_view = OrderSteps.as_view(FORMS)

def order_wizard_view(request, id_template):

    return order_view(request, id_template)



@require_POST
def set_currency(request, currency):

    reponse = redirect('index')

    reponse.set_cookie('currency', currency )

    return reponse


@staff_member_required
def dashboard(request):


    c = Client.objects.all().count
    o = Order.objects.filter(is_deal=True)
    o_c = Order.objects.all().count
    d = Order.objects.filter(is_deal=True).count

    # TODO: MUST Improve this



    m4 = Order.objects.filter(created_date__year=2017, created_date__month=04).count
    m5 = Order.objects.filter(created_date__year=2017, created_date__month=05).count
    m6 = Order.objects.filter(created_date__year=2017, created_date__month=06).count
    m7 = Order.objects.filter(created_date__year=2017, created_date__month=07).count

    income = 0

    for oi in o:
        income = income + oi.get_total_amount_order()




    context = admin.site.each_context(request)
    context.update({
        'c':c,
        'o_c': o_c,
        'd': d,
        'income': income,
        'm4': m4,
        'm5': m5,
        'm6': m6,
        'm7': m7,
    })

    template = 'admin/index.html'
    return render(request, template, context)


def invoice(request, id_order):

    order = Order.objects.get(id=id_order)
    client = Client.objects.get(id=order.client_id)

    params = {
        "order": order,
        "client": client,
    }

    context= admin.site.each_context(request)
    context.update({
    })

    template = 'invoice.html'
# send -> params**
    return render(request, template, context)