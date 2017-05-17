from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^steps/(?P<id_template>\d+)', views.order_wizard_view, name='steps'),
    url(r'^set-currency/(?P<currency>[\w\-]+)/', views.set_currency, name='set-currency'),
    url(r'^admin/dash/$', views.dashboard, name='admin-dash'),
    url(r'^invoice/(?P<id_order>\d+)', views.invoice, name='invoice'),
]