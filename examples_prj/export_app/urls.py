from django.conf.urls import patterns, include, url
from export_app.views import *


urlpatterns = patterns('',

    url(r'^form$', BookSearchView.as_view(), name='dispositivo_list'),

)