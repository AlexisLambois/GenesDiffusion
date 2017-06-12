'''
Created on 9 juin 2017

@author: alexis
'''
from django.shortcuts import render

def save_view(request):
    return render(request,'form/save.html',{})