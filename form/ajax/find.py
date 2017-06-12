'''
Created on 26 avr. 2017

Recherche de Cheptel/Race/Preleveur sur la page admin

@author: alexis
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from form.manager.racemanager import RaceManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.preleveurmanager import PreleveurManager

@csrf_exempt
def go_find(request):
    
    """ Recuperation de la table correspondant a la recherche et du numero de l'objet x recherche """
    
    table = request.POST.get('table')
    id = request.POST.get('input_id')
    
    """ Verification de saisie null """
    
    if id == "":
        return HttpResponse("None")
    
    """ On considere la recherche echoue a l'initialisation """
    
    data = "Null"
    
    """ On remplace les data si la recherche est un succes """
    
    if table == 'race':
        find = RaceManager.get_race_by({"numero":"='" + str(id) + "'"})
        if len(find) != 0 : data = find[0].get_nom()
    elif table == 'cheptel':
        find = CheptelManager.get_cheptel_by({"numero":"='" + str(id) + "'"})
        if len(find) != 0 : data = find[0].get_detenteur()
    else:
        find = PreleveurManager.get_preleveur_by({"numero":"='" + str(id) + "'"})
        if len(find) != 0 : data = find[0].get_nom()
    
    return HttpResponse(data)