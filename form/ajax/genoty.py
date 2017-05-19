'''
Created on 11 mai 2017

Affichage des data sur la page de recherche/consultation 

@author: alexis
'''
from django.http import HttpResponse
from form.manager.genotypage_prelevementmanager import Genotypage_PrelevementManager
import json


""" Tableau des noms sql des colonnes dans l'ordre de saisie """

tab_entete = ["form_genotypage.plaque","form_genotypage.position","format_puce","date_debut","date_scan","callrate","link_to_file","note","date_insertion","form_prelevement.plaque","form_prelevement.position","date_enregistrement","date_demande","date_extraction","date_reception_lille","type_materiel","dosage","conformite_dosage","code_barre","nombre_extraction","echec_extraction","statut_vcg","animal_id","preleveur_id"]

def go_genoty(request):
    
    """ Recuperation de tout les champs de saisie ainsi que de l'indice de ceux remplis """
    
    indice = []
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
    
    data = []
    
    """ Affichage initial sans recherche """
    
    if len(indice) == 0:
        temp = Genotypage_PrelevementManager.get_fusion()

        for row in temp:
            data.append(row.to_array())
            
    else:
        tosql_genotype = {}
        tosql_prelevement = {}
        
        for id in indice:
            if id < 8 :
                tosql_genotype.update({tab_entete[id]:inputs[id].lower()})
            else:
                tosql_prelevement.update({tab_entete[id]:inputs[id].lower()})
        
        data_temp = Genotypage_PrelevementManager.get_fusion_by(tosql_genotype,tosql_prelevement)
        
        for row in data_temp:
            data.append(row.to_array())
            
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

