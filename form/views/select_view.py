'''
Created on 25 avr. 2017

@author: alexis
'''
from ..manager.animalmanager import AnimalManager
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def select_view(request):
    return render(request,'form/index.html',{'data_animal': AnimalManager.get_all_animals()})
