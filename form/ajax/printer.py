'''
Created on 11 mai 2017

@author: alexis
'''
from django.http import HttpResponse
from form.manager.prelevementmanager import PrelevementManager
import json,os,csv,time
from django.conf import settings
from form.models import prelevement
from form.manager.racemanager import RaceManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.animalmanager import AnimalManager
from form.manager.preleveurmanager import PreleveurManager
from django.views.decorators.csrf import csrf_exempt

tab_entete = ["date_insertion","plaque","position","date_enregistrement","date_demande","date_extraction","date_reception_lille","type_materiel","dosage","conformite_dosage","code_barre","nombre_extraction","echec_extraction","statut_vcg","ordre","date_insertion","numero","nom","sexe","date_naissance","pere","mere","pays","jumeau","numero","detenteur","numero","nom","preleveur_id","nom"]

def go_print(request):
    
    indice = []
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
    
    data = []
    
    if len(indice) == 0:
        temp = PrelevementManager.get_all_prelevements()

        for row in temp:
            data.append(row.to_array_html())
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
                data.append((PrelevementManager.get_prelevement_by_beta({"auto_increment_id":id_prelevement})[0]).to_array_html())
            
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
