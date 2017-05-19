'''
Created on 17 mai 2017

@author: alexis
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from form.manager.genotypage_prelevementmanager import Genotypage_PrelevementManager

@csrf_exempt
def truc_view(request):
    for row in Genotypage_PrelevementManager.get_fusion():
        print(row.to_array())
    return render(request,'form/truc.html',{})