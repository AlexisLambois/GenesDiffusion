import json,collections,os,time,csv
from django.http import HttpResponse
from ..manager.animalmanager import AnimalManager
from ..manager.racemanager import RaceManager
from ..models.race import Race
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from form.manager.cheptelmanager import CheptelManager

tab_entete = ["ordre","date_insertion","numero","nom","sexe","date_naissance","pere","mere","pays","jumeau","race_id","nom","cheptel_id","detenteur"]

def go_select(request):
       
    indice = []
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
       
    text = []
    if len(indice) == 0:

        temp = AnimalManager.get_all_animals()
        
        if request.GET.get('ordre') == "true": 
            temp = sort_by_ordre(temp)
        for row in temp:
            text.append(row.to_array())
    else:
        tosql = {}
        
        for id in indice:
            if id == 11 :
                races = RaceManager.get_race_by_alpha({tab_entete[id]:inputs[id]})
                for race in races:  
                    tosql.update({"race_id":race.get_numero()})
            elif id == 13 :
                cheptels = CheptelManager.get_cheptel_by_alpha({tab_entete[id]:inputs[id]})
                for cheptel in cheptels:  
                    tosql.update({"cheptel_id":cheptel.get_numero()})
            else:
                tosql.update({tab_entete[id]:inputs[id]})
        animals = AnimalManager.get_animal_by_alpha(tosql)
        
        if request.GET.get('ordre') == "true":
            animals = sort_by_ordre(animals)
        
        for animal in animals:
            text.append(animal.to_array())
            
    data = json.dumps(text)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def go_save(request):
    animals = []
    indice = []
    for i in request.POST.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.POST.getlist('inputs[]')

    if len(indice) == 0:
        animals = AnimalManager.get_all_animals()
    else:
        tosql = {}
        
        for id in indice:
            if id == 11 :
                races = RaceManager.get_race_by_alpha({tab_entete[id]:inputs[id]})
                for race in races:  
                    tosql.update({"race_id":race.get_numero()})
            elif id == 13 :
                cheptels = CheptelManager.get_cheptel_by_alpha({tab_entete[id]:inputs[id]})
                for cheptel in cheptels:  
                    tosql.update({"cheptel_id":cheptel.get_numero()})
            else:
                tosql.update({tab_entete[id]:inputs[id]})
        animals = AnimalManager.get_animal_by_alpha(tosql)
    
        if request.GET.get('ordre') == "true":
            animals = sort_by_ordre(animals)

    data = write_to_file(animals)
    return HttpResponse(data)  

def write_to_file(data):
    if not os.path.exists(settings.BASE_DIR+"/media/save/"):
        os.mkdir(settings.BASE_DIR+"/media/save/")    
    
    w_file=open(str(settings.BASE_DIR+"/media/save/save"+time.strftime('%d_%m_%y_%H_%M',time.localtime())+".csv"), 'w')
        
    c = csv.writer(w_file, delimiter='\t', lineterminator='\n')
    
    c.writerow(["Ordre","Date Insertion","Id","Nom","Sexe","Date de Naissance","Pere","Mere","Pays","Jumeau","Numero Race","Nom Race","Cheptel Actuel","Detenteur Actuel"])    
    
    for animal in data: 
        c.writerow([animal.get_ordre(),animal.get_date_insertion(),animal.get_numero(),animal.get_nom(),animal.get_sexe(),animal.get_date_naissance(),animal.get_pere(),animal.get_mere(),animal.get_jumeau(),animal.get_pays(),animal.get_race().get_numero(),animal.get_race().get_nom(),animal.get_cheptel().get_numero(),animal.get_cheptel().get_detenteur()])
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