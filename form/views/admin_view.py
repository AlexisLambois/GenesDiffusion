'''
Created on 26 avr. 2017

@author: alexis
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from form.manager.racemanager import RaceManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.preleveurmanager import PreleveurManager
from form.models.race import Race
from form.models.cheptel import Cheptel
from form.models.preleveur import Preleveur
import os,time
from django.conf import settings

@csrf_exempt
def admin_view(request):
    
    """ Insertion de l'objet correspondant """
    
    if request.method == 'POST':
        
        id = request.POST.get('input')
        table = request.POST.get('table')
        attribut = request.POST.get('attribut')
        
        if table == "race":
            RaceManager.register(Race.create(id,attribut.upper()))
        elif table == "cheptel":
            CheptelManager.register(Cheptel.create(id,attribut.upper()))
        else:
            PreleveurManager.register(Preleveur.create(id, attribut.upper()))
            
        write_to_log(table,id,attribut)
    return render(request,'form/admin.html',{})

def write_to_log(table,id,attribut):
    
    if not os.path.exists(settings.BASE_DIR+"/media/logs/"):
        os.mkdir(settings.BASE_DIR+"/media/logs/")    
    
    fichier = open(str(settings.BASE_DIR+"/media/logs/log"+time.strftime('%d_%m_%y_%H_%M',time.localtime())), "a")
    fichier.write("Addons du : " + time.strftime('%d/%m/%y %H:%M',time.localtime()) + " sur database : " + table + "\n")
    fichier.write("\t"+str(table)+" numero : "+str(id)+" nouvelle attribut : "+str(attribut)+"\n")
    fichier.close()
    return str(settings.BASE_DIR+"/media/logs/log"+time.strftime('%d_%m_%y_%H_%M',time.localtime()))
