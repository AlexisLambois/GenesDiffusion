'''
Created on 11 mai 2017

Affichage des data sur la page de recherche/consultation 

@author: alexis
'''
from django.http import HttpResponse
from form.manager.prelevementmanager import PrelevementManager
import json,os,csv,time,collections
from django.conf import settings
from form.manager.racemanager import RaceManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.animalmanager import AnimalManager
from form.manager.preleveurmanager import PreleveurManager
from django.views.decorators.csrf import csrf_exempt
from form.manager.databasemanager import DatabaseManager

""" Tableau des noms sql des colonnes dans l'ordre de saisie """

tab_entete = ["date_insertion","plaque","position","date_enregistrement","date_demande","date_extraction","date_reception_lille","type_materiel","dosage","conformite_dosage","code_barre","nombre_extraction","echec_extraction","statut_vcg","ordre","date_insertion","numero","nom","sexe","date_naissance","pere","mere","pays","jumeau","numero","detenteur","numero","nom","preleveur_id","nom"]

@csrf_exempt
def go_print(request):
    
    """ Recuperation de tout les champs de saisie ainsi que de l'indice de ceux remplis """
    
    indice = []
    for i in request.POST.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.POST.getlist('inputs[]')
    operateurs = request.POST.getlist('operateurs[]')
    
    data = []
    
    """ Affichage initial sans recherche """
    
    if len(indice) == 0:
        temp = PrelevementManager.get_all_prelevements()

        for row in temp:
            data.append(row.to_array_html())
            
    else:
        
        """ Cas de recherche """
        search_race = []
        search_cheptel = []
        search_animal = []
        search_preleveur = []
        search_prelevement = []
        """ Pour chaque changement on verifie quelle table doit recevoir une requete """
        
        for id in indice:
            if id > 11 and id <=23 :
                search_animal.append(id)
            elif id == 24 or id == 25:
                search_cheptel.append(id)
            elif id == 26 or id == 27:
                search_race.append(id)
            elif id == 29:
                search_preleveur.append(id)
            else:
                search_prelevement.append(id)
                
        temp = {}
        for id in search_cheptel:
            print(id)
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_cheptel = CheptelManager.get_cheptel_by_gamma(temp)
        
        temp.clear()
        
        for id in search_race:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_race = RaceManager.get_race_by_gamma(temp)
        temp.clear()
        
        for id in search_preleveur:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_preleveur = PreleveurManager.get_preleveur_by_gamma(temp)
        
        temp.clear()
        
        for id in search_animal:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_animal = AnimalManager.get_animal_by_gamma(temp,{"cheptel_id":requete_cheptel,"race_id":requete_race})
        
        temp.clear()
        
        for id in search_prelevement:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_prelevement = PrelevementManager.get_prelevement_by_gamma(temp,{"animal_id":requete_animal,"preleveur_id":requete_preleveur})
        
        temp.clear()
        
        data_temp = DatabaseManager.execute(requete_prelevement)
        data_temp = PrelevementManager.to_object(data_temp)
        for row in data_temp:
            data.append(row.to_array_html())
          
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def go_save(request):
    
    indice = []
    for i in request.POST.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.POST.getlist('inputs[]')
    operateurs = request.POST.getlist('operateurs[]')
    
    data = []
    
    if len(indice) == 0:
        temp = PrelevementManager.get_all_prelevements()

        for row in temp:
            data.append(row)
    else:

        """ Cas de recherche """
        search_race = []
        search_cheptel = []
        search_animal = []
        search_preleveur = []
        search_prelevement = []
        """ Pour chaque changement on verifie quelle table doit recevoir une requete """
        
        for id in indice:
            if id > 11 and id <=23 :
                search_animal.append(id)
            elif id == 24 or id == 25:
                search_cheptel.append(id)
            elif id == 26 or id == 27:
                search_race.append(id)
            elif id == 29:
                search_preleveur.append(id)
            else:
                search_prelevement.append(id)
                
        temp = {}
        for id in search_cheptel:
            print(id)
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_cheptel = CheptelManager.get_cheptel_by_gamma(temp)
        
        temp.clear()
        
        temp = {}
        for id in search_race:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_race = RaceManager.get_race_by_gamma(temp)
        
        temp.clear()

        for id in search_preleveur:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_preleveur = PreleveurManager.get_preleveur_by_gamma(temp)
        
        temp.clear()

        for id in search_animal:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_animal = AnimalManager.get_animal_by_gamma(temp,{"cheptel_id":requete_cheptel,"race_id":requete_race})
        
        temp.clear()

        for id in search_prelevement:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_prelevement = PrelevementManager.get_prelevement_by_gamma(temp,{"animal_id":requete_animal,"preleveur_id":requete_preleveur})
        
        temp.clear()
        
        data_temp = DatabaseManager.execute(requete_prelevement)
        data_temp = PrelevementManager.to_object(data_temp)
        for row in data_temp:
            data.append(row.to_array_html())
                
    write_to_file(data)
    return HttpResponse(data)  

def write_to_file(data):
    
    if not os.path.exists(settings.BASE_DIR+"/media/save/"):
        os.mkdir(settings.BASE_DIR+"/media/save/")    
    
    w_file=open(str(settings.BASE_DIR+"/media/save/save"+time.strftime('%d_%m_%y_%H_%M',time.localtime())+".csv"), 'w')
        
    c = csv.writer(w_file, delimiter='\t', lineterminator='\n')
    
    c.writerow(tab_entete)    
    for prelve in data: 
        c.writerow(prelve)
    w_file.close()  

def sort_by_ordre(tab_animal):
    temp = {}
    for animal in tab_animal:
        temp.update({animal:animal.get_ordre()})
    temp = collections.OrderedDict(sorted(temp.items(),key=lambda x:x[1]))
    tab_animal = []
    for animal,ordre in temp.iteritems():
        tab_animal.append(animal)
    return tab_animal
