#! /usr/bin/python
#-*- coding:UTF8 -*-
import time,os,re
from form.manager.animalmanager import AnimalManager
from form.manager.prelevementmanager import PrelevementManager
from form.manager.genotypagemanager import GenotypageManager
from form.models.animal import Animal
from form.models.prelevement import Prelevement
from form.models.genotypage import Genotypage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse

@csrf_exempt
def go_insert(request):
    
    """ 
    Insertion d un objet x a partir d un fichier 
    """
    
    addons_animal = []
    addons_prelevement = []
    addons_genotypage = []
    total = []
    i = 1
    
    #Recuperation des donnees
    
    while True:
        data = request.POST.getlist('data['+str(i)+'][]')
        total.append(data)
        i=i+1 
        if not len(data) != 0: break
    total.pop()
    
    #Recuperation ordre dans titre fichier
    
    ordre = filename_analyse(total[len(total)-2][0])
    table = total[len(total)-1][0]
    
    if table.lower() == "animal":
        
        #Traitements des donnees
        
        for j in range(0,len(total)-2):
            
            #Reperage champs vide
            
            for colonne in range(0,len(total[j])):
                if(total[j][colonne] == ""):
                    total[j][colonne] = 0
                else:
                    total[j][colonne] = total[j][colonne].upper()
            
            #Creation et insertion animal
            
            animal_temp = Animal.create(total[j][0],total[j][1],total[j][2],total[j][3],total[j][4],total[j][5],total[j][6],total[j][7],ordre,time.strftime('%d-%m-%y',time.localtime()),total[j][8],total[j][9])
            AnimalManager.register(animal_temp)
            addons_animal.append(total[j][0])
            
    elif table.lower() == "prelevement" :
        
        #Traitements des donnees
        
        for j in range(0,len(total)-2):
            
            #Reperage champs vide
            
            for colonne in range(0,len(total[j])):
                if(total[j][colonne] == ""):
                    total[j][colonne] = 0
                else:
                    total[j][colonne] = total[j][colonne].upper()
            
            #Creation et insertion prelevement
            
            prelev_temp = Prelevement.create(total[j][0],total[j][1],total[j][2],total[j][3],total[j][4],total[j][5],total[j][6],total[j][7],total[j][8],total[j][9],total[j][10],total[j][11],total[j][12],time.strftime('%d-%m-%y',time.localtime()),total[j][13],total[j][14])
            PrelevementManager.register(prelev_temp)
            addons_prelevement.append(total[j][0])
    else :
        
        #Traitements des donnees
        
        for j in range(0,len(total)-2):
            
            #Reperage champs vide
            
            for colonne in range(0,len(total[j])):
                if(total[j][colonne] == ""):
                    total[j][colonne] = 0
                else:
                    total[j][colonne] = total[j][colonne].upper()
            
            #Creation et insertion prelevement
            
            genoty_temp = Genotypage.create(total[j][0],total[j][1],total[j][2],total[j][3],total[j][4],total[j][5],total[j][6],total[j][7],total[j][8],total[j][9])
            GenotypageManager.register(genoty_temp)
            addons_genotypage.append(total[j][0])
            
    #Ecriture en log des ajouts fait
    
    data = (str(write_to_log(addons_animal,addons_prelevement,total[len(total)-2][0])))
    return HttpResponse(data)       

def filename_analyse(filename):
    
    """
    Recherche du l indice ordre dans le nom du fichier si il est present : present = indice / absent = 000
    """
    
    try:
        ordre = str(filename[filename.index('_')+1:filename.index('.')])
        if re.match(r"^[0-9]+$",ordre) is not None : 
            return ordre
    except ValueError:
        return "000"

def write_to_log(animal_array,prelevement_array,filename):
    
    """
    Ecriture des donnes inserees dans un fichier log avec sa date d ecriture comme nom
    """
    
    if not os.path.exists(settings.BASE_DIR+"/media/logs/"):
        os.mkdir(settings.BASE_DIR+"/media/logs/")    
    
    fichier = open(str(settings.BASE_DIR+"/media/logs/log"+time.strftime('%d_%m_%y_%H_%M',time.localtime())), "a")
    fichier.write("Addons du : " + time.strftime('%d/%m/%y %H:%M',time.localtime()) + " sur fichier " + filename + "\n")
    
    fichier.write("     Ajout/Update Animal : \n")
    for id_animal in animal_array:
        fichier.write("          Animal numero : " + str(id_animal) + "\n")
    
    fichier.write("     Ajout/Update Prelevement : \n")
    for id_prelev in prelevement_array:
        fichier.write("          Prelevement numero : " + str(id_prelev) + "\n")
        
    fichier.close()
    return str(settings.BASE_DIR+"/media/logs/log"+time.strftime('%d_%m_%y_%H_%M',time.localtime()))
