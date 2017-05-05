'''
Created on 26 avr. 2017

@author: alexis
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..manager.racemanager import RaceManager
from ..manager.cheptelmanager import CheptelManager
from ..manager.preleveurmanager import PreleveurManager

@csrf_exempt
def go_find(request):
    table = request.POST.get('table')
    id = request.POST.get('input_id')
    
    # Cas de champs vide
    if id == "":
        return HttpResponse("None")
    
    #Si Race ou Cheptel pas trouve
    data = "Null"
    
    # Cas de champs remplie
    if table == 'race':
        find = RaceManager.get_race_by_beta({"numero":str(id)})
        if len(find) != 0 : data = find[0].get_nom()
    elif table == 'cheptel':
        find = CheptelManager.get_cheptel_by_beta({"numero":str(id)})
        if len(find) != 0 : data = find[0].get_detenteur()
    else:
        find = PreleveurManager.get_preleveur_by_beta({"numero":str(id)})
        if len(find) != 0 : data = find[0].get_nom()
    
    return HttpResponse(data)