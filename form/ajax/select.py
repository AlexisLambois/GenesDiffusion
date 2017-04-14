import json,sys
from django.http import Http404, HttpResponse
from ..manager.animalmanager import AnimalManager
from ..manager.racemanager import RaceManager
from ..manager.cheptelmanager import CheptelManager

def go_select(request):
       
       indice = []
       for i in request.GET.getlist('indice[]'):
              indice.append(int(i))
       inputs = request.GET.getlist('inputs[]')
       
       text = ""
       if len(indice) == 0:
              for row in AnimalManager.get_all_animals():
                     text += row.to_html()
              data = json.dumps(str(text))
       else:
              numBovin = []
              for row in saisieByIndice(indice[0],inputs[indice[0]]):                         
                     numBovin.append(row.get_numero())              
              
              for i in range(1,len(indice)):
                     var = []
                     for row in saisieByIndice(indice[i],inputs[indice[i]]):                         
                            if row.get_numero() in numBovin:
                                   var.append(row.get_numero())
                     numBovin = var             
                                   
              animals = []
              for y in numBovin:
                     animals.append(AnimalManager.get_animal_by_numero(y))
                                     
              for j in animals:                      
                     text += j[0].to_html()
                                
              data = json.dumps(str(text))
              
       return HttpResponse(data, content_type='application/json')

def zero(string):
       return AnimalManager.get_animal_by_numero(string)
def one(string):
       return AnimalManager.get_animal_by_nom(string)
def two(string):
       return AnimalManager.get_animals_by_sexe(string)
def three(string):
       return AnimalManager.get_animals_by_date_naissance(string)
def four(string):
       return AnimalManager.get_animals_by_pere(string)
def five(string):
       return AnimalManager.get_animals_by_mere(string)
def six(string):
       return AnimalManager.get_animals_by_pays(string)
def seven(string):
       return AnimalManager.get_all_animals()
def eight(string):
       return RaceManager.get_race_by_numero(string)
def nine(string):
       return RaceManager.get_races_by_nom(string)
def ten(string):
       return CheptelManager.get_cheptel_by_numero(string)
def eleven(string):
       return CheptelManager.get_cheptels_by_detenteur(string)

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
       } 
       return options[indice](string)  
