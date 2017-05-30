'''
Created on 11 mai 2017

@author: alexis
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def print_view(request):
    return render(request,'form/print.html',{})