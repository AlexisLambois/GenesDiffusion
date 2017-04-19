#! /usr/bin/python
#-*- coding:UTF8 -*-
import sys
from django.shortcuts import render
from ..manager.animalmanager import *
from ..models.animal import Animal
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def go_insert(request):
    
    data = request.POST.getlist('data[0][]')
    sys.stdout.write(str(data))
    sys.stdout.flush() 
    for int in range(0,len(data)):
        animal_temp = Animal.create(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
    
    AnimalManager.register(animal_temp)
    
    return render(request,'form/index.html',{})        

def data_csv_gather(filename):
    mon_fichier = open(filename,"r")
    data = []
    with mon_fichier as f:
        reader = csv.reader(f)
        for row in reader: 
            data.append(row[0].split('\t'))
    mon_fichier.close()
    return data