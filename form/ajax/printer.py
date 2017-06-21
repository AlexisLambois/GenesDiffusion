'''
Created on 11 mai 2017

Affichage des data sur la page de recherche/consultation 

@author: alexis
'''
from django.http import HttpResponse
from form.manager.prelevementmanager import PrelevementManager
import json,os,csv,time,collections,re
from django.conf import settings
from form.manager.racemanager import RaceManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.animalmanager import AnimalManager
from form.manager.preleveurmanager import PreleveurManager
from django.views.decorators.csrf import csrf_exempt
from form.manager.databasemanager import DatabaseManager

""" Tableau des noms sql des colonnes dans l'ordre de saisie """

tab_entete = ["date_insertion","plaque","position","date_enregistrement","date_demande","date_extraction","date_reception_lille","type_materiel","dosage","conformite_dosage","code_barre","nombre_extraction","echec_extraction","statut_vcg","ordre","date_insertion","numero","nom","sexe","date_naissance","pere","mere","pays","jumeau","numero","detenteur","numero","nom","preleveur_id","nom"]

@csrf_exempt
def go_print(request):
    
    """ Recuperation de tout les champs de saisie ainsi que de l'indice de ceux remplis """
    
    indice = []
    for i in request.POST.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.POST.getlist('inputs[]')
    operateurs = request.POST.getlist('operateurs[]')
    
    data = []
    
    """ Affichage initial sans recherche """
    
    if len(indice) == 0:
        data = PrelevementManager.get_prelevement_to_html([])
            
    else:
        
        """ Cas de recherche """
        
        search_race = []
        search_cheptel = []
        search_animal = []
        search_preleveur = []
        search_prelevement = []
        
        """ Pour chaque changement on verifie quelle table doit recevoir une requete """
        
        for id in indice:
            if id > 11 and id <=23 :
                search_animal.append(id)
            elif id == 24 or id == 25:
                search_cheptel.append(id)
            elif id == 26 or id == 27:
                search_race.append(id)
            elif id == 29:
                search_preleveur.append(id)
            else:
                search_prelevement.append(id)
                
        temp = {}
        
        """ On construit une requete concernant la table cheptel en pretant bie attention si la recherche est faites sur une date """
        
        for id in search_cheptel:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_cheptel = CheptelManager.get_cheptel_sous_requete(temp)
        
        temp.clear()
        
        """ On construit une requete concernant la table race en pretant bie attention si la recherche est faites sur une date """
        
        for id in search_race:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_race = RaceManager.get_race_sous_requete(temp)
        
        temp.clear()
        
        """ On construit une requete concernant la table preleveur en pretant bie attention si la recherche est faites sur une date """
        
        for id in search_preleveur:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_preleveur = PreleveurManager.get_preleveur_sous_requete(temp)
        
        temp.clear()
        
        """ On construit une requete concernant la table animal en pretant bie attention si la recherche est faites sur une date 
            La difference ici est qu on ajoute les requetes de cheptel et race pour construire une requete compose de ses sous requete"""
        
        for id in search_animal:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_animal = AnimalManager.get_animal_sous_requete(temp,{"cheptel_id":requete_cheptel,"race_id":requete_race})
        
        temp.clear()
        
        """ On construit une requete concernant la table prelevement en pretant bie attention si la recherche est faites sur une date 
            La difference ici est qu on ajoute les requetes de animal et preleveur pour construire une requete compose de ses sous requete"""
            
        for id in search_prelevement:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_prelevement = PrelevementManager.get_prelevement_sous_requete(temp,{"animal_id":requete_animal,"preleveur_id":requete_preleveur})
        
        temp.clear()
        
        """ On execute la requete construite tout au long du programme """
        
        data_temp = DatabaseManager.execute(requete_prelevement)

        """ On va chercher le code html garder en table pour aller plus vite """
        
        data = PrelevementManager.get_prelevement_to_html(data_temp)
          
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def go_save(request):
    
    indice = []
    for i in request.POST.getlist('indice[]'):
        indice.append(int(i))
    inputs = request.POST.getlist('inputs[]')
    operateurs = request.POST.getlist('operateurs[]')
    case_cocher = []
    for i in request.POST.getlist('case_cocher[]'):
        case_cocher.append(int(i))
        
    data = []
    
    if len(case_cocher) == 0 :
        return HttpResponse(data)
    
    if len(indice) == 0:
        
        data = PrelevementManager.get_prelevement_to_html([])
    
    else:

        """ Cas de recherche """
        
        search_race = []
        search_cheptel = []
        search_animal = []
        search_preleveur = []
        search_prelevement = []
        
        """ Pour chaque changement on verifie quelle table doit recevoir une requete """
        
        for id in indice:
            if id > 11 and id <=23 :
                search_animal.append(id)
            elif id == 24 or id == 25:
                search_cheptel.append(id)
            elif id == 26 or id == 27:
                search_race.append(id)
            elif id == 29:
                search_preleveur.append(id)
            else:
                search_prelevement.append(id)
                
        temp = {}
        
        """ On construit une requete concernant la table cheptel en pretant bie attention si la recherche est faites sur une date """
        
        for id in search_cheptel:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_cheptel = CheptelManager.get_cheptel_sous_requete(temp)
        
        temp.clear()
        
        """ On construit une requete concernant la table race en pretant bie attention si la recherche est faites sur une date """
        
        for id in search_race:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_race = RaceManager.get_race_sous_requete(temp)
        
        temp.clear()
        
        """ On construit une requete concernant la table preleveur en pretant bie attention si la recherche est faites sur une date """
        
        for id in search_preleveur:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_preleveur = PreleveurManager.get_preleveur_sous_requete(temp)
        
        temp.clear()
        
        """ On construit une requete concernant la table animal en pretant bie attention si la recherche est faites sur une date 
            La difference ici est qu on ajoute les requetes de cheptel et race pour construire une requete compose de ses sous requete"""
        
        for id in search_animal:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_animal = AnimalManager.get_animal_sous_requete(temp,{"cheptel_id":requete_cheptel,"race_id":requete_race})
        
        temp.clear()
        
        """ On construit une requete concernant la table prelevement en pretant bie attention si la recherche est faites sur une date 
            La difference ici est qu on ajoute les requetes de animal et preleveur pour construire une requete compose de ses sous requete"""
            
        for id in search_prelevement:
            if operateurs[id] == "":
                temp.update({tab_entete[id]:inputs[id]})
            else:
                temp.update({tab_entete[id]:str(operateurs[id]+"'"+inputs[id]+"'")})
        requete_prelevement = PrelevementManager.get_prelevement_sous_requete(temp,{"animal_id":requete_animal,"preleveur_id":requete_preleveur})
        
        temp.clear()
        
        """ On execute la requete construite tout au long du programme """
        
        data_temp = DatabaseManager.execute(requete_prelevement)

        """ On va chercher le code html garder en table pour aller plus vite """
        
        data = PrelevementManager.get_prelevement_to_html(data_temp)
    
    data_temp = []
    re1='>(.*?)<'
    
    """ Savegarde d une partie des colonnes precisees dans case_cocher """
    
    if len(case_cocher) != 30:  
        
        for row in data:
            temp = re.findall(re1, row[0])
            row_temp = []
            for num in case_cocher:
                row_temp.append(temp[(num*2+1)])
            data_temp.append(row_temp)
        
    else:
        
        """ Sauvegarde de toutes les colonnes en parsant le code html """
         
        for row in data:
            temp = re.findall(re1, row[0])
            row_temp = []
            for id_champ in range(0,len(temp)):
                if id_champ%2 != 0:
                    row_temp.append(temp[id_champ])
            data_temp.append(row_temp)
            
    data = data_temp
        
    write_to_file(data)
    return HttpResponse(data)  

def write_to_file(data):
    
    if not os.path.exists(settings.BASE_DIR+"/media/save/"):
        os.mkdir(settings.BASE_DIR+"/media/save/")    
    
    w_file=open(str(settings.BASE_DIR+"/media/save/save"+time.strftime('%d_%m_%y_%H_%M',time.localtime())+".csv"), 'w')
        
    c = csv.writer(w_file, delimiter='\t', lineterminator='\n')
    
    c.writerow(tab_entete)    
    for prelve in data: 
        c.writerow(prelve)
    w_file.close()  

""" Sort sur la colonne ordre """
#Methode non utilise

def sort_by_ordre(tab_animal):
    temp = {}
    for animal in tab_animal:
        temp.update({animal:animal.get_ordre()})
    temp = collections.OrderedDict(sorted(temp.items(),key=lambda x:x[1]))
    tab_animal = []
    for animal,ordre in temp.iteritems():
        tab_animal.append(animal)
    return tab_animal
