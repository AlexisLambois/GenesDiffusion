'''
Created on 11 mai 2017

Affichage des data sur la page de recherche/consultation 

@author: alexis
'''
from django.http import HttpResponse
from form.manager.genotypage_prelevementmanager import Genotypage_PrelevementManager
import json,os,time,csv
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import numpy as np

""" Tableau des noms sql des colonnes dans l'ordre de saisie """

tab_entete = ["form_genotypage.plaque","form_genotypage.position","format_puce","date_debut","date_scan","callrate","link_to_file","note","date_insertion","form_prelevement.plaque","form_prelevement.position","date_enregistrement","date_demande","date_extraction","date_reception_lille","type_materiel","dosage","conformite_dosage","code_barre","nombre_extraction","echec_extraction","statut_vcg","animal_id","preleveur_id"]

def go_genoty(request):
    
    """ Recuperation de tout les champs de saisie ainsi que de l'indice de ceux remplis """
    
    indice = []
    for i in request.GET.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.GET.getlist('inputs[]')
    operateurs = request.GET.getlist('operateurs[]')
    
    data = []
  
    """ Affichage initial sans recherche """
    
    if len(indice) == 0:
        temp = Genotypage_PrelevementManager.get_fusion()

        for row in temp:
            data.append(row.to_html())
            
    else:
        
        """ Recherche avec les saisie : 
            superieur a 8 on interroge la table genotypage 
            sinon la table prelevement """
            
        tosql_genotype = {}
        tosql_prelevement = {}
        
        for id in indice:
            
            """ id represente ici sur quelle colonne se place le notre curseur de recherche ex: id=0 est la colonne form_genotypage.plaque ( cf tab_entete )"""
            
            if id < 8 :
                
                """ On separe les dates des autres recherches :
                    si un operateur ( sup,inf ou egal) n'est pas present sur la colonne numero id on effectue une requete simple
                    sinon on modifie la requete en ajoutant un operateur """
                
                if operateurs[id] == "":
                    tosql_genotype.update({tab_entete[id]:inputs[id]})
                else:
                    tosql_genotype.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
            else:
                if operateurs[id] == "":
                    tosql_prelevement.update({tab_entete[id]:inputs[id]})
                else:
                    tosql_prelevement.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        
        """ On demande la fusion avec les recherches faites sur les deux tables """
        
        data_temp = Genotypage_PrelevementManager.get_fusion_by(tosql_genotype,tosql_prelevement)

        for row in data_temp:
            data.append(row.to_html())
            
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def go_save(request):
    
    """ Idem que go_genoty, on recupere les infos selectionnees """
    
    indice = []
    for i in request.POST.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.POST.getlist('inputs[]')
    operateurs = []
    for i in request.POST.getlist('operateurs[]'):
        operateurs.append((i))
        
    """ Avec en plus les colonnes demandees par l utilisateur """
    
    case_cocher = []
    for i in request.POST.getlist('case_cocher[]'):
        case_cocher.append(int(i))
    
    data = []
    
    """ Si rien est demande on ne fait aucune sauvegarde """
    
    if len(case_cocher) == 0 :
        return HttpResponse(data)
    
    """ Cas de recherche sans criteres """
    
    if len(indice) == 0:
        data_temp = Genotypage_PrelevementManager.get_fusion()
            
    else:
        tosql_genotype = {}
        tosql_prelevement = {}
        
        for id in indice:
            
            """ id represente ici sur quelle colonne se place le notre curseur de recherche ex: id=0 est la colonne form_genotypage.plaque ( cf tab_entete )"""
            
            if id < 8 :
                
                """ On separe les dates des autres recherches :
                    si un operateur ( sup,inf ou egal) n'est pas present sur la colonne numero id on effectue une requete simple
                    sinon on modifie la requete en ajoutant un operateur """
                    
                if operateurs[id] == "":
                    tosql_genotype.update({tab_entete[id]:inputs[id]})
                else:
                    tosql_genotype.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
            else:
                if operateurs[id] == "":
                    tosql_prelevement.update({tab_entete[id]:inputs[id]})
                else:
                    tosql_prelevement.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
                    
        """ On demande la fusion avec les recherches faites sur les deux tables """
        
        data_temp = Genotypage_PrelevementManager.get_fusion_by(tosql_genotype,tosql_prelevement)

    """ Cas ou l utilisateur veut toutes les colonnes """
    
    if len(case_cocher) == 24:
        for row in data_temp:
            data.append(row.to_array())
    else:
        
        """ Cas ou on recupere que les colonnes presentes dans case_cocher """
        
        data_second = []
        
        for row in data_temp:
            data_second.append(row.to_array())
            
        data_second = np.array(data_second)

        data = data_second[:, case_cocher]
        
    """ Ecrture dans un csv des lignes et colonnes selectionnees """
    
    write_to_file(data)
    return HttpResponse(data)  

def write_to_file(data):
    
    if not os.path.exists(settings.BASE_DIR+"/media/save/"):
        os.mkdir(settings.BASE_DIR+"/media/save/")    
    
    w_file=open(str(settings.BASE_DIR+"/media/save/save"+time.strftime('%d_%m_%y_%H_%M',time.localtime())+".csv"), 'w')
        
    c = csv.writer(w_file, delimiter='\t', lineterminator='\n')
    
    c.writerow(tab_entete)    
    for genoty in data: 
        c.writerow(genoty)
    w_file.close()    

