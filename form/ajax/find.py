'''
Created on 26 avr. 2017

@author: alexis
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..manager.racemanager import RaceManager
from ..manager.cheptelmanager import CheptelManager
@csrf_exempt
def go_find(request):
    table = request.POST.get('table')
    id = request.POST.get('input_id')
    
    if id == "":
        return HttpResponse("None")
    print(id)
    data = "Null"
    if table == 'race':
        find = RaceManager.get_race_by_numero(str(id))
        print(find)
        if len(find) != 0 : data = find[0].get_nom()
        print(data)
    else:
        find = CheptelManager.get_cheptel_by_numero(str(id))
        if len(find) != 0 : data = find[0].get_detenteur()
    
    return HttpResponse(data)