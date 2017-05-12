from django.conf.urls import url
from .ajax import select
from .ajax import insert
from .ajax import find
from form.ajax import printer
from .views import insert_view
from .views import admin_view 
from form.views import print_view

urlpatterns = [
    url(r'^print/$', print_view.print_view, name='print_view'),
    url(r'^insert/$', insert_view.insert_view, name='insert_view'),
    url(r'^admin/$', admin_view.admin_view, name='admin_view'),
    url(r'^ajax/printer/$', printer.go_print),
    url(r'^ajax/add/$', insert.go_insert),
    url(r'^ajax/save/$', printer.go_save),
    url(r'^ajax/find/$', find.go_find)
]
