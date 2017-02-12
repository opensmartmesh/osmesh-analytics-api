from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'(?P<node>[0-9]{10})/$', views.measure, name='measure'),
    url(r'^$', views.measure, name='sense_index'),
]
