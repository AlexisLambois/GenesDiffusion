from django.conf.urls import url
from form.ajax import insert
from form.ajax import find
from form.ajax import printer
from form.ajax import genoty
from form.views import insert_view
from form.views import admin_view 
from form.views import print_view
from form.views import truc_view
from form.views import genotypage_view

urlpatterns = [
    url(r'^print/$', print_view.print_view, name='print_view'),
    url(r'^insert/$', insert_view.insert_view, name='insert_view'),
    url(r'^admin/$', admin_view.admin_view, name='admin_view'),
    url(r'^test/$', truc_view.truc_view, name='truc_view'),
    url(r'^genotypage/$', genotypage_view.genotypage_view, name='genotypage_view'),
    url(r'^ajax/printer/$', printer.go_print),
    url(r'^ajax/add/$', insert.go_insert),
    url(r'^ajax/save/$', printer.go_save),
    url(r'^ajax/find/$', find.go_find),
    url(r'^ajax/genoty/$', genoty.go_genoty)
]
