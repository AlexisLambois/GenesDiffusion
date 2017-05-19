'''
Created on 11 mai 2017

Affichage des data sur la page de recherche/consultation 

@author: alexis
'''
from django.http import HttpResponse
from form.manager.prelevementmanager import PrelevementManager
import json,os,csv,time,collections
from django.conf import settings
from form.models import prelevement
from form.manager.racemanager import RaceManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.animalmanager import AnimalManager
from form.manager.preleveurmanager import PreleveurManager
from django.views.decorators.csrf import csrf_exempt
from form.manager.databasemanager import DatabaseManager

""" Tableau des noms sql des colonnes dans l'ordre de saisie """

tab_entete = ["date_insertion","plaque","position","date_enregistrement","date_demande","date_extraction","date_reception_lille","type_materiel","dosage","conformite_dosage","code_barre","nombre_extraction","echec_extraction","statut_vcg","ordre","date_insertion","numero","nom","sexe","date_naissance","pere","mere","pays","jumeau","numero","detenteur","numero","nom","preleveur_id","nom"]

def go_print(request):
    
    """ Recuperation de tout les champs de saisie ainsi que de l'indice de ceux remplis """
    
    indice = []
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
    
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
            temp.update({tab_entete[id]:inputs[id].lower()})
        requete_cheptel = CheptelManager.get_cheptel_by_gamma(temp)
        
        temp.clear()
        
        temp = {}
        for id in search_race:
            temp.update({tab_entete[id]:inputs[id].lower()})
        requete_race = RaceManager.get_race_by_gamma(temp)
        temp.clear()
        
        temp = {}
        for id in search_preleveur:
            temp.update({tab_entete[id]:inputs[id].lower()})
        requete_preleveur = PreleveurManager.get_preleveur_by_gamma(temp)
        
        temp.clear()
        
        temp = {}
        for id in search_animal:
            temp.update({tab_entete[id]:inputs[id].lower()})
        requete_animal = AnimalManager.get_animal_by_gamma(temp,{"cheptel_id":requete_cheptel,"race_id":requete_race})
        
        temp.clear()
        
        temp = {}
        for id in search_prelevement:
            temp.update({tab_entete[id]:inputs[id].lower()})
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
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
    
    data = []
    
    if len(indice) == 0:
        temp = PrelevementManager.get_all_prelevements()

        for row in temp:
            data.append(row)
    else:

        prelevements = []
        
        for id in indice:
            if id > 14 and id <=23 :
                
                animals = AnimalManager.get_animal_by_alpha({tab_entete[id]:inputs[id]})
                for animal in animals:
                    temp = PrelevementManager.get_prelevement_by_alpha({"animal_id":animal.get_numero()})
                    id = []
                    for prelevement in temp:
                        id.append(prelevement.get_id())
                    prelevements = prelevements + id
            elif id == 24 or id == 25:
                
                cheptels = CheptelManager.get_cheptel_by_alpha({tab_entete[id]:inputs[id]})
                animals = []
                for cheptel in cheptels:  
                    animals.append(AnimalManager.get_animal_by_alpha({"cheptel_id":cheptel.get_numero()}))
                
                for tab_animal in animals: 
                    for animal in tab_animal: 
                        temp = PrelevementManager.get_prelevement_by_alpha({"animal_id":animal.get_numero()})
                        id = []
                        for prelevement in temp:
                            id.append(prelevement.get_id())
                        if len(prelevements) != 0 :
                            prelevements = [val for val in prelevements if val in id]
                        else:
                            prelevements = id
                        
            elif id == 26 or id == 27:
                
                races = RaceManager.get_race_by_alpha({tab_entete[id]:inputs[id]})
                animals = []
                for race in races:  
                    animals.append(AnimalManager.get_animal_by_alpha({"race_id":race.get_numero()}))
                
                for tab_animal in animals: 
                    for animal in tab_animal: 
                        temp = PrelevementManager.get_prelevement_by_alpha({"animal_id":animal.get_numero()})
                        id = []
                        for prelevement in temp:
                            id.append(prelevement.get_id())
                        if len(prelevements) != 0 :
                            prelevements = [val for val in prelevements if val in id]
                        else:
                            prelevements = id

            elif id == 29:
                
                preleveurs = PreleveurManager.get_preleveur_by_alpha({tab_entete[id]:inputs[id]})
                for preleveur in preleveurs:
                    temp = PrelevementManager.get_prelevement_by_alpha({"preleveur_id":preleveur.get_numero()})
                    id = []
                    for prelevement in temp:
                        id.append(prelevement.get_id())
                    if len(prelevements) != 0 :
                        prelevements = [val for val in prelevements if val in id]
                    else:
                        prelevements = id
            else:
                
                temp = PrelevementManager.get_prelevement_by_alpha({tab_entete[id]:inputs[id]})
                id = []
                for prelevement in temp:
                    id.append(prelevement.get_id())
                if len(prelevements) != 0 :
                    prelevements = [val for val in prelevements if val in id]
                else:
                    prelevements = id
         
        for id_prelevement in prelevements:
                data.append((PrelevementManager.get_prelevement_by_beta({"auto_increment_id":id_prelevement})[0]))
                
    write_to_file(data)
    return HttpResponse(data)  

def write_to_file(data):
    if not os.path.exists(settings.BASE_DIR+"/media/save/"):
        os.mkdir(settings.BASE_DIR+"/media/save/")    
    
    w_file=open(str(settings.BASE_DIR+"/media/save/save"+time.strftime('%d_%m_%y_%H_%M',time.localtime())+".csv"), 'w')
        
    c = csv.writer(w_file, delimiter='\t', lineterminator='\n')
    
    c.writerow(["Date Insertion","Plaque","Position","Date Enregistrement","Date Demande","Date Extraction","Date Reception Lille","Type de Materiel","Dosage","Conformite","Code Barre","Nombre Extraction","Echec Extraction","Statut VCG","Ordre","Date Insertion","Id","Nom","Sexe","Date de Naissance","Pere","Mere","Pays","Jumeau","Numero Race","Nom Race","Cheptel Actuel","Detenteur Actuel","Numero Agrement","Nom"])    
    print(data)
    for animal in data: 
        c.writerow(animal.to_array_html())
    w_file.close()    

    return str(settings.BASE_DIR+"/media/save/save"+time.strftime('%d_%m_%y_%H_%M',time.localtime()))

def sort_by_ordre(tab_animal):
    temp = {}
    for animal in tab_animal:
        temp.update({animal:animal.get_ordre()})
    temp = collections.OrderedDict(sorted(temp.items(),key=lambda x:x[1]))
    tab_animal = []
    for animal,ordre in temp.iteritems():
        tab_animal.append(animal)
    return tab_animal
