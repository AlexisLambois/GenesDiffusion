from django.conf.urls import url,include
from . import views
from .ajax import select
from .ajax import insert

urlpatterns = [
   url(r'^$', views.create_view, name='create_view'),
   url(r'^insert/$', views.insert_view, name='insert_view'),
   url(r'^ajax/more/$', select.go_select),
]
