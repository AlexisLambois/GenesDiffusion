'''
Created on 18 mai 2017

@author: alexis
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def genotypage_view(request):
    return render(request,'form/genotypage.html',{})