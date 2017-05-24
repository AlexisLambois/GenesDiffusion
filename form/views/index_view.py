'''
Created on 24 mai 2017

@author: alexis
'''
from django.shortcuts import render

def index_view(request):
    return render(request,'form/index.html',{})