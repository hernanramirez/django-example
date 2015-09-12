from django.conf.urls import patterns, include, url
from export_app.views import *


urlpatterns = patterns('',

    url(r'^form$', BookSearchView.as_view(), name='form'),
    url(r'^form_modal$', BookModalExportView.as_view(), name='form_modal'),
    url(r'^books$', BookList.as_view(), name='books_list'),

)