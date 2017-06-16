from django.conf.urls import url
from form.ajax import insert
from form.ajax import find
from form.ajax import printer
from form.ajax import genoty
from form.views import insert_view
from form.views import admin_view 
from form.views import print_view
from form.views import genotypage_view
from form.views import index_view
from form.auto_scripts import insert_auto

urlpatterns = [
    
    # Url d afficahge 
    url(r'^$', index_view.index_view, name='index_view'),
    url(r'^print/$', print_view.print_view, name='print_view'),
    url(r'^insert/$', insert_view.insert_view, name='insert_view'),
    url(r'^admin/$', admin_view.admin_view, name='admin_view'),
    url(r'^genotypage/$', genotypage_view.genotypage_view, name='genotypage_view'),
    url(r'^test/$', insert_auto.start, name='insert_auto'),
    
    # Url d action
    url(r'^ajax/printer/$', printer.go_print),
    url(r'^ajax/add/$', insert.go_insert),
    url(r'^ajax/save/$', printer.go_save),
    url(r'^ajax/save_geno/$', genoty.go_save),
    url(r'^ajax/find/$', find.go_find),
    url(r'^ajax/genoty/$', genoty.go_genoty)
]
