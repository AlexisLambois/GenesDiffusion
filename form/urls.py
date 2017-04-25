from django.conf.urls import url
from .ajax import select
from .ajax import insert
from .views import select_view
from .views import insert_view
from .views import update_view

urlpatterns = [
    url(r'^$', select_view.select_view, name='create_view'),
    url(r'^insert/$', insert_view.insert_view, name='insert_view'),
    url(r'^update/$', update_view.update_view, name='update_view'),
    url(r'^ajax/more/$', select.go_select),
    url(r'^ajax/add/$', insert.go_insert),
    url(r'^ajax/save/$', select.go_save),
]
