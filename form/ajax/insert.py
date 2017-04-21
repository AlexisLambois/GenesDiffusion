#! /usr/bin/python
#-*- coding:UTF8 -*-
import sys,json,time,os
from django.shortcuts import render
from ..manager.animalmanager import *
from ..manager.racemanager import *
from ..manager.cheptelmanager import *
from ..models.animal import Animal
from ..models.race import Race
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import Http404, HttpResponse

@csrf_exempt
def go_insert(request):
    addons_race = []
    addons_cheptel = []
    addons_animal = []
    champs_vide = []
   
    total = []
    i = 1
    while True:
        data = request.POST.getlist('data['+str(i)+'][]')
        total.append(data)
        i=i+1 
        if not len(data) != 0: break
    total.pop()
    
    for j in range(0,len(total)):
        
        for colonne in range(0,len(total[j])):
            if(total[j][colonne] == ""):
                total[j][colonne] = 0
                champs_vide.append("Champs ligne : " + str(j+1) + " colonne : " + str(colonne+1))
                
        if(len(RaceManager.get_race_by_numero(total[j][8])) == 0):
            RaceManager.register(Race.create(total[j][8],total[j][9]))
            if total[j][8] not in addons_race : addons_race.append(total[j][8])
            
        if(len(CheptelManager.get_cheptel_by_numero(total[j][10])) == 0):
            CheptelManager.register(Cheptel.create(total[j][10],total[j][11]))
            if total[j][10] not in addons_cheptel : addons_cheptel.append(total[j][10])
            
        animal_temp = Animal.create(total[j][0],total[j][1],total[j][2],total[j][3],total[j][4],total[j][5],total[j][6],total[j][7],total[j][8],total[j][10])
        AnimalManager.register(animal_temp)
        addons_animal.append(total[j][0])
        
    data = format_html(str(write_to_log(addons_animal,addons_cheptel,addons_race,champs_vide)))
    return HttpResponse(data)       

def write_to_log(animal_array,cheptel_array,race_array,champs_vide):
    
    if not os.path.exists(settings.BASE_DIR+"/media/logs/"):
        os.mkdir(settings.BASE_DIR+"/media/logs/")    
    
    fichier = open(str(settings.BASE_DIR+"/media/logs/log"+time.strftime('%d_%m_%y_%H_%M',time.localtime())), "a")
    fichier.write("Addons du : " + time.strftime('%d/%m/%y %H:%M',time.localtime()) + "\n")
    
    fichier.write("     Ajout/Update Animal : \n")
    for id_animal in animal_array:
        fichier.write("          Animal numero : " + str(id_animal) + "\n")
    
    fichier.write("     Ajout/Update Race : \n")
    for id_race in race_array:
        fichier.write("          Race numero : " + str(id_race) + "\n")        
   
    fichier.write("     Ajout/Update Cheptel : \n")
    for id_cheptel in cheptel_array:
        fichier.write("          Cheptel numero : " + str(id_cheptel) + "\n")  
    
    fichier.write("     Champs Vide : \n")
    for champs in champs_vide:
        fichier.write("          " + champs + "\n")    
    
    fichier.close()
    return str(settings.BASE_DIR+"/media/logs/log"+time.strftime('%d_%m_%y_%H_%M',time.localtime()))