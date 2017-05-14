from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.step_1, name='step-1'),
    url(r'^step2/(?P<id_template>\d+)', views.step_2, name='step-2'),
    url(r'^step3/$', views.step_3, name='step-3'),
]