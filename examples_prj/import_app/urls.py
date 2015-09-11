from django.conf.urls import patterns, include, url

from import_app.views import FileList, FileNew, FileDelete, ImportView


urlpatterns = patterns('',

    url(r'^file/list$', FileList.as_view(), name='file_list'),
    url(r'^file/new$', FileNew.as_view(), name='file_new'),
    url(r'^file/delete/(?P<pk>\d+)$', FileDelete.as_view(), name='file_delete'),
    url(r'^file/import$', ImportView.as_view(), name='file_new'),

)
