from django.conf.urls import patterns, include, url
from perfis.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name='convidar')
)
