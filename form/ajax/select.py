import json,collections,os,time,csv
from django.http import HttpResponse
from ..manager.animalmanager import AnimalManager
from ..manager.racemanager import RaceManager
from ..manager.cheptelmanager import CheptelManager
from ..models.animal import Animal
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def go_select(request):
       
    indice = []
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
       
    text = ""
    if len(indice) == 0:
        temp = AnimalManager.get_all_animals()
        if request.GET.get('ordre') == "true": 
            temp = sort_by_ordre(temp)
        for row in temp:
            text += row.to_html()
    else:
        numBovin = []
     
        for row1 in saisieByIndice(indice[0],inputs[indice[0]]):
            if not isinstance(row1, Animal):
                for row2 in row1:                         
                    numBovin.append(row2.get_numero())   
            else:
                numBovin.append(row1.get_numero())   
                          
            for i in range(1,len(indice)):
                var = []
                for row1 in saisieByIndice(indice[i],inputs[indice[i]]):
                    if not isinstance(row1, Animal):
                        for row2 in row1:                                  
                            if row2.get_numero() in numBovin:
                                var.append(row2.get_numero())
                    else:
                        if row1.get_numero() in numBovin:
                            var.append(row1.get_numero())                                   
                numBovin = var             
                                   
        animals = []
        for y in numBovin:
            animals.append(AnimalManager.get_animal_by_numero(y)[0])
        
        if request.GET.get('ordre') == "true": 
            animals = sort_by_ordre(animals)                     
        for j in animals:                      
            text += j.to_html()
                                
    data = json.dumps(str(text))
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
        numBovin = []

        for row1 in saisieByIndice(indice[0],inputs[indice[0]]):
            if not isinstance(row1, Animal):
                for row2 in row1:                         
                    numBovin.append(row2.get_numero())   
            else:
                numBovin.append(row1.get_numero())   

        for i in range(1,len(indice)):
            var = []
            for row1 in saisieByIndice(indice[i],inputs[indice[i]]):
                if not isinstance(row1, Animal):
                    for row2 in row1:                                  
                        if row2.get_numero() in numBovin:
                            var.append(row2.get_numero())
                else:
                    if row1.get_numero() in numBovin:
                        var.append(row1.get_numero())                                   
            numBovin = var             

        for y in numBovin:
            animals.append(AnimalManager.get_animal_by_numero(y)[0])
    
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

def zero(string):
    return AnimalManager.get_animals_by_ordre(string)
def one(string):
    return AnimalManager.get_animals_by_date_insertion(string)
def two(string):
    return AnimalManager.get_animal_by_numero(string)
def three(string):
    return AnimalManager.get_animal_by_nom(string)
def four(string):
    return AnimalManager.get_animals_by_sexe(string)
def five(string):
    return AnimalManager.get_animals_by_date_naissance(string)
def six(string):
    return AnimalManager.get_animals_by_pere(string)
def seven(string):
    return AnimalManager.get_animals_by_mere(string)
def eight(string):
    return AnimalManager.get_animals_by_pays(string)
def nine(string):
    return AnimalManager.get_all_animals()
def ten(string):
    return AnimalManager.get_animals_by_id_race(string)
def eleven(string):
    id_animal = []
    for race in RaceManager.get_race_by_nom(string):
        id_animal.append(AnimalManager.get_animals_by_id_race(race.get_numero()))
    return id_animal       
def twelve(string):
    return AnimalManager.get_animals_by_id_cheptel(string)
def thirteen(string):
    id_animal = []
    for cheptel in CheptelManager.get_cheptel_by_detenteur(string):
        id_animal.append(AnimalManager.get_animals_by_id_cheptel(cheptel.get_numero()))
    return id_animal

def saisieByIndice(indice,string):
    options = {
              0 : zero,
              1 : one,
              2 : two,
              3 : three,
              4 : four,
              5 : five,
              6 : six,
              7 : seven,
              8 : eight,
              9 : nine,
              10 : ten,
              11 : eleven,
              12 : twelve,
              13 : thirteen 
    } 
    return options[indice](string)  

def sort_by_ordre(tab_animal):
    temp = {}
    for animal in tab_animal:
        temp.update({animal:animal.get_ordre()})
    temp = collections.OrderedDict(sorted(temp.items(),key=lambda x:x[1]))
    tab_animal = []
    for animal,ordre in temp.iteritems():
        tab_animal.append(animal)
    return tab_animal