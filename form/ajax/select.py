import json,sys
from django.http import Http404, HttpResponse
from ..manager.animalmanager import AnimalManager
from ..manager.racemanager import RaceManager
from ..manager.cheptelmanager import CheptelManager
from ..models.animal import Animal

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
       return AnimalManager.get_animals_by_id_race(string)
def nine(string):
       id_animal = []
       for race in RaceManager.get_race_by_nom(string):
              id_animal.append(AnimalManager.get_animals_by_cheptel(cheptel.get_numero()))
       return id_animal       
def ten(string):
       return AnimalManager.get_animals_by_cheptel(string)
def eleven(string):
       id_animal = []
       for cheptel in CheptelManager.get_cheptel_by_detenteur(string):
              id_animal.append(AnimalManager.get_animals_by_cheptel(cheptel.get_numero()))
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
       } 
       return options[indice](string)  
