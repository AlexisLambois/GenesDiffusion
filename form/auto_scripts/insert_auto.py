'''
Created on 16 juin 2017

@author: alexis
'''

from django.conf import settings
import os,csv,re,time,shutil
from django.http import HttpResponse
from pyexcel_ods import get_data
from openpyxl import load_workbook
from form.manager.cheptelmanager import CheptelManager
from form.manager.racemanager import RaceManager
from form.manager.preleveurmanager import PreleveurManager
from form.manager.animalmanager import AnimalManager
from form.manager.prelevementmanager import PrelevementManager
from form.manager.genotypagemanager import GenotypageManager
from form.models.animal import Animal
from form.models.prelevement import Prelevement
from form.models.genotypage import Genotypage

""" Repertoire de stockage et extensions possible """

dossier = "/resultats"
logs = "/logs"
archive = "/archive"
file_to_insert = "/file_to_insert"
error = "/error"
extensions = [".csv",".ods",".xlsx",".xls"]

def start(request):
    
    set_up_file() #Creation des repertoires si ils nexistent pas
    
    """ Recuperation de la liste des fichiers present dans le repertoire """
    
    fichier_all = os.listdir(settings.BASE_DIR+dossier+file_to_insert)
    temp1 = []
    temp2 = []
    temp3 = []
    
    """ Sort des fichiers par ordre d insertion """
    
    for fichier in fichier_all:
        if(re.match(r"^animal",str(fichier)) is not None):
            temp1.append(str(fichier))
        elif(re.match(r"^prelevement",str(fichier)) is not None):
            temp2.append(str(fichier))
        elif(re.match(r"^genotypage",str(fichier)) is not None):
            temp3.append(str(fichier))
      
    fichier_all = temp1+temp2+temp3
     
    """ Retour vide en cas ou il n'y a rien a inserer """
    
    if len(fichier_all) == 0 : return HttpResponse()
    
    """ Pour chaque fichier on verifie l extension et la nomenclature du fichier """
    
    for i in fichier_all:
        
        extension = os.path.splitext(settings.BASE_DIR+dossier+file_to_insert+"/"+i)[1]
        
        bool_table = re.match(r"^animal|^prelevement|^genotypage",str(i)) is not None
        
        if extension in extensions and bool_table:
            
            """ Recuperation des donnnees dans fichier """
            
            data = data_gather(settings.BASE_DIR+dossier+file_to_insert+"/"+i, extension)
            table = i[0:i.index('_')]
            
            if table == "animal" and len(data[0]) == 10 :
                
                """ Verfie la validite des donnnees """
                
                if analyse_data_animal(data,settings.BASE_DIR+dossier+file_to_insert+"/"+i) == 1 :
                    
                    """ On effectue l insertion en base """
                    
                    insert(data,settings.BASE_DIR+dossier+file_to_insert+"/"+i,"animal")
                    
                    """ On deplace le fichier dans le repertoire correspondant """ 
                    
                    shutil.move(settings.BASE_DIR+dossier+file_to_insert+"/"+i, settings.BASE_DIR+dossier+archive+"/")
                    
                else:
                    shutil.move(settings.BASE_DIR+dossier+file_to_insert+"/"+i, settings.BASE_DIR+dossier+error+"/")
                    
            elif table == "prelevement" and len(data[0]) == 15:
                
                """ Verfie la validite des donnnees """
                
                if analyse_data_prelev(data,settings.BASE_DIR+dossier+file_to_insert+"/"+i) == 1 :
                    
                    """ On effectue l insertion en base """
                    
                    insert(data,settings.BASE_DIR+dossier+file_to_insert+"/"+i,"prelevement")
                    
                    """ On deplace le fichier dans le repertoire correspondant """ 
                    
                    shutil.move(settings.BASE_DIR+dossier+file_to_insert+"/"+i, settings.BASE_DIR+dossier+archive+"/")
                    
                else:
                    shutil.move(settings.BASE_DIR+dossier+file_to_insert+"/"+i, settings.BASE_DIR+dossier+error+"/")
                    
            elif table == "genotypage" and len(data[0]) == 10 :
                
                """ Verfie la validite des donnnees """
                
                if analyse_data_genoty(data,settings.BASE_DIR+dossier+file_to_insert+"/"+i) == 1 :
                    
                    """ On effectue l insertion en base """
                    
                    insert(data,settings.BASE_DIR+dossier+file_to_insert+"/"+i,"genotypage")
                    
                    """ On deplace le fichier dans le repertoire correspondant """ 
                    
                    shutil.move(settings.BASE_DIR+dossier+file_to_insert+"/"+i, settings.BASE_DIR+dossier+archive+"/")
                    
                else:
                    shutil.move(settings.BASE_DIR+dossier+file_to_insert+"/"+i, settings.BASE_DIR+dossier+error+"/")
                    
            else:
                print("ERREUR")
                
    return HttpResponse()

def set_up_file():
    
    """ Creation des repertoires de stockage si ils nexistent pas """
    
    if not os.path.exists(settings.BASE_DIR+dossier):
        os.mkdir(settings.BASE_DIR+dossier)
    
    if not os.path.exists(settings.BASE_DIR+dossier+logs):
        os.mkdir(settings.BASE_DIR+dossier+logs)
        
    if not os.path.exists(settings.BASE_DIR+dossier+archive):
        os.mkdir(settings.BASE_DIR+dossier+archive)
        
    if not os.path.exists(settings.BASE_DIR+dossier+file_to_insert):
        os.mkdir(settings.BASE_DIR+dossier+file_to_insert)
        
    if not os.path.exists(settings.BASE_DIR+dossier+error):
        os.mkdir(settings.BASE_DIR+dossier+error)
        
def data_gather(filename,extension):
    
    """ Collecte des donnnees selon le type dextension """
    
    data = []
    
    if extension == ".csv":
        mon_fichier = open(filename,"r")
        with mon_fichier as f:
            reader = csv.reader(f)
            for row in reader: 
                data.append(row[0].split('\t'))
        mon_fichier.close()
        
    elif extension == ".ods" or extension == ".xls":
        data = (get_data(filename,start_column=0, column_limit=15)).values()[0]
        
    elif extension == ".xlsx":
        data = []
        wb = load_workbook(filename=filename, read_only=True)
        ws = wb[wb.get_sheet_names()[0]]
        for row in ws.rows:
            temp = []
            for cell in row:
                temp.append(cell.value)
            data.append(temp)
            
    return data

def analyse_data_animal(data,filename):
    
    error_finded = ["\n\nErreur : fichier :"+filename+"\n"]
    
    for row in range(1,len(data)) :
        if re.match(r"^[A-Z0-9]{9,20}$",str(data[row][0]).upper()) is None : 
            error_finded.append("\n["+str(row)+",0] : "+str(data[row][0]).upper()+" / ^[A-Z0-9]{9,20}$")
        if re.match(r"^[A-Z0-9]+([ ]*[-]*[A-Z0-9]*)*$",str(data[row][1]).upper()) is None :  
            error_finded.append("\n["+str(row)+",1] : "+str(data[row][1]).upper()+" / ^[A-Z0-9]+([ ]*[-]*[A-Z0-9]*)*$")
        if re.match(r"^[0-9]{1}$",str(data[row][2]).upper()) is None :  
            error_finded.append("\n["+str(row)+",2] : "+str(data[row][2]).upper()+" / ^[0-9]{1}$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][3]).upper()) is None :  
            error_finded.append("\n["+str(row)+",3] : "+str(data[row][3]).upper()+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^[A-Z0-9]{5,20}$",str(data[row][4]).upper())is None :  
            error_finded.append("\n["+str(row)+",4] : "+str(data[row][4]).upper()+" / ^[A-Z0-9]{5,20}$")
        if re.match(r"^[A-Z0-9]{5,20}$",str(data[row][5]).upper())is None :
            error_finded.append("\n["+str(row)+",5] : "+str(data[row][5]).upper()+" / ^[A-Z0-9]{5,20}$")
        if re.match(r"^[A-Z]{2}$",str(data[row][6]).upper())is None :
            error_finded.append("\n["+str(row)+",6] : "+str(data[row][6]).upper()+" / ^[A-Z]{2}$")
        if re.match(r"^(FALSE|TRUE)$",str(data[row][7]).upper())is None :
            error_finded.append("\n["+str(row)+",7] : "+str(data[row][7]).upper()+" / ^(FALSE|TRUE)$")
        if len(CheptelManager.get_cheptel_by({"numero":str(data[row][8]).upper()})) == 0 :
            error_finded.append("\n["+str(row)+",8] : "+str(data[row][8]).upper()+" / Cheptel inexistant")
        if len(RaceManager.get_race_by({"numero":str(data[row][9]).upper()})) == 0 :
            error_finded.append("\n["+str(row)+",9] : "+str(data[row][9]).upper()+" / Race inexistant")
    
    if len(error_finded) != 1 :
        insert_in_log(error_finded)
    
    return len(error_finded)

def analyse_data_prelev(data,filename):
    
    error_finded = ["\n\nErreur : fichier :"+filename+"\n"]
    
    for row in range(1,len(data)) :
        if re.match(r"^[A-Z0-9]{7,23}[-]*[A-Z0-9]*$",str(data[row][0]).upper()) is None : 
            error_finded.append("\n["+str(row)+",0] : "+str(data[row][0]).upper()+" / ^[A-Z0-9]{7,23}[-]*[A-Z0-9]*$")
        if re.match(r"^[A-Z0-9]{0,3}$",str(data[row][1]).upper()) is None :  
            error_finded.append("\n["+str(row)+",1] : "+str(data[row][1]).upper()+" / ^[A-Z0-9]{0,3}$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][2]).upper()) is None :  
            error_finded.append("\n["+str(row)+",2] : "+str(data[row][2]).upper()+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][3]).upper()) is None :  
            error_finded.append("\n["+str(row)+",3] : "+str(data[row][3]).upper()+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][4]).upper())is None :  
            error_finded.append("\n["+str(row)+",4] : "+str(data[row][4].upper())+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][5]).upper())is None :
            error_finded.append("\n["+str(row)+",5] : "+str(data[row][5]).upper()+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^[A-Z0-9]{0,20}$",str(data[row][6]).upper())is None :
            error_finded.append("\n["+str(row)+",6] : "+str(data[row][6]).upper()+" / ^[A-Z0-9]{0,20}$")
        if re.match(r"^[0-9]{1,3}\.?[0-9]{1,2}$",str(data[row][7]).upper())is None :
            error_finded.append("\n["+str(row)+",7] : "+str(data[row][7]).upper()+" / ^[0-9]{1,3}\.?[0-9]{1,2}$")
        if re.match(r"^(FALSE|TRUE)$",str(data[row][8]).upper())is None :
            error_finded.append("\n["+str(row)+",8] : "+str(data[row][8]).upper()+" / ^(FALSE|TRUE)$")
        if re.match(r"^[A-Z0-9]{0,10}$",str(data[row][9]).upper())is None :
            error_finded.append("\n["+str(row)+",9] : "+str(data[row][9]).upper()+" / ^[A-Z0-9]{0,10}$")
        if re.match(r"^[0-9]*$",str(data[row][10]).upper())is None :
            error_finded.append("\n["+str(row)+",10] : "+str(data[row][10]).upper()+" / ^[0-9]*$")
        if re.match(r"^[A-Z0-9]*$",str(data[row][11]).upper())is None :
            error_finded.append("\n["+str(row)+",11] : "+str(data[row][11]).upper()+" / ^[A-Z0-9]*$")
        if re.match(r"^[0-9]{2}$",str(data[row][12]).upper())is None :
            error_finded.append("\n["+str(row)+",12] : "+str(data[row][12]).upper()+" / ^[0-9]{2}$")
        if len(AnimalManager.get_animal_by({"numero":str(data[row][13]).upper()})) == 0 :
            error_finded.append("\n["+str(row)+",13] : "+str(data[row][13]).upper()+" / Animal inexistant")
        if len(PreleveurManager.get_preleveur_by({"numero":str(data[row][14]).upper()})) == 0 :
            error_finded.append("\n["+str(row)+",14] : "+str(data[row][14]).upper()+" / Preleveur inexistant")
    
    if len(error_finded) != 1 :
        insert_in_log(error_finded)
    
    return len(error_finded)

def analyse_data_genoty(data,filename):
    
    error_finded = ["\n\nErreur : fichier :"+filename+"\n"]
    
    for row in range(1,len(data)) :
        if re.match(r"^[A-Z0-9]{7,23}[-]*[A-Z0-9]*$",str(data[row][0]).upper()) is None : 
            error_finded.append("\n["+str(row)+",0] : "+str(data[row][0]).upper()+" / ^[A-Z0-9]{7,23}[-]*[A-Z0-9]*$")
        if re.match(r"^[A-Z0-9]{0,3}$",str(data[row][1]).upper()) is None :  
            error_finded.append("\n["+str(row)+",1] : "+str(data[row][1]).upper()+" / ^[A-Z0-9]{0,3}$")
        if re.match(r"^[A-Z0-9]{0,20}$",str(data[row][2]).upper()) is None :  
            error_finded.append("\n["+str(row)+",2] : "+str(data[row][2]).upper()+" / ^[A-Z0-9]{0,20}$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][3]).upper()) is None :  
            error_finded.append("\n["+str(row)+",3] : "+str(data[row][3]).upper()+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[row][4]).upper())is None :  
            error_finded.append("\n["+str(row)+",4] : "+str(data[row][4].upper())+" / ^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$")
        if re.match(r"^[0-9]{1,3}\.?[0-9]{1,2}$",str(data[row][5]).upper())is None :
            error_finded.append("\n["+str(row)+",5] : "+str(data[row][5]).upper()+" / ^[0-9]{1,3}\.?[0-9]{1,2}$")
        if re.match(r"^[A-Z0-9]{0,20}$",str(data[row][6]).upper())is None :
            error_finded.append("\n["+str(row)+",6] : "+str(data[row][6]).upper()+" / ^[A-Z0-9]{0,20}$")
        if len(PrelevementManager.get_prelevement_by({"plaque":str(data[row][8]),"position":str(data[row][9])})) == 0 :
            error_finded.append("\n["+str(row)+",8]["+str(row)+",9] : "+str(data[row][8]).upper()+" "+str(data[row][9]).upper()+" / Prelevement inexistant")
    
    if len(error_finded) != 1 :
        insert_in_log(error_finded)
    
    return len(error_finded)
    
def insert(data,filename,table):
    
    if table == "animal":
        
        to_log_insert = insert_animals(data, filename)
        
    elif table == "prelevement":
        
        to_log_insert = insert_prelev(data,filename)
        
    elif table == "genotypage":
        
        to_log_insert = insert_genoty(data, filename)
        
    insert_in_log(to_log_insert[0])
    for i in range(1,len(to_log_insert)):
        insert_in_log(to_log_insert[i])
        
    return True
       
def insert_in_log(tab):
    
    fichier = open(str(settings.BASE_DIR+dossier+logs+"/log_"+time.strftime('%d%m%Y_%Hh%M',time.localtime())), "a")
    for i in tab:
        fichier .write(str(i))
    fichier.close()
      
def insert_animals(data,filename):
    
    i = os.path.split(filename)[0]
    temp = i[i.index('_')+1:]
    ordre = temp[:temp.index('_')]
    
    to_log_insert = [["\n\nLes elements ayant etait ajoutes/modifie : fichier : "+filename+"\n"]]
        
    for row in range(1,len(data)):
            
        temp_log = ["\nanimal "+data[row][0]+"|"]
            
        old_animal = AnimalManager.get_animal_by({"numero":data[row][0]})
                                     
        if len(old_animal) != 0:
                
            old_animal = old_animal[0].to_array()
                
            for champ in range(1,len(data[row])):
                    
                temp = data[row][champ]
                    
                if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(temp)) is not None:
                    temp = str(temp[6:10]+"-"+temp[3:5]+"-"+temp[0:2])
                        
                if str(temp) != str(old_animal[champ+2]):
                    temp_log.append(data[0][champ]+" : "+str(old_animal[champ+2])+" to "+str(temp)+"|")
                        
        else:
            for champ in range(1,len(data[row])):
                temp_log.append(str(data[row][champ])+"|")
                    
        if len(temp_log) == 1:
            to_log_insert.append(["\nNone modif animal "+data[row][0]])
        else:
            to_log_insert.append(temp_log)    
               
        animal_temp = Animal.create(data[row][0],data[row][1],data[row][2],data[row][3],data[row][4],data[row][5],data[row][6],data[row][7],ordre,time.strftime('%d-%m-%y',time.localtime()),data[row][8],data[row][9])
        AnimalManager.register(animal_temp) 
        
    return to_log_insert    

def insert_prelev(data,filename):
        
    to_log_insert = [["\n\nLes elements ayant etait ajoutes/modifie : fichier : "+filename+"\n"]]
        
    for row in range(1,len(data)):
            
        temp_log = ["\nprelevement "+data[row][0]+"|"]
            
        old_preleve = PrelevementManager.get_prelevement_by({"plaque":data[row][0],"position":data[row][1]})
                                     
        if len(old_preleve) != 0:
                
            old_preleve = old_preleve[0].to_array()
                
            for champ in range(1,len(data[row])):
                    
                temp = data[row][champ]
                    
                if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(temp)) is not None:
                    temp = str(temp[6:10]+"-"+temp[3:5]+"-"+temp[0:2])
                        
                if str(temp) != str(old_preleve[champ]):
                    temp_log.append(data[0][champ]+" : "+str(old_preleve[champ])+" to "+str(temp)+"|")
                        
        else:
            for champ in range(1,len(data[row])):
                temp_log.append(str(data[row][champ])+"|")
                    
        if len(temp_log) == 1:
            to_log_insert.append(["\nNone modif prelevement "+data[row][0]])
        else:
            to_log_insert.append(temp_log)    
               
        preleve_temp = Prelevement.create(data[row][0],data[row][1],data[row][2],data[row][3],data[row][4],data[row][5],data[row][6],data[row][7],data[row][8],data[row][9],data[row][10],data[row][11],data[row][12],time.strftime('%d-%m-%y',time.localtime()),data[row][13],data[row][14])
        PrelevementManager.register(preleve_temp) 
        
    return to_log_insert

def insert_genoty(data,filename):
    
    to_log_insert = [["\n\nLes elements ayant etait ajoutes/modifie : fichier : "+filename+"\n"]]
        
    for row in range(1,len(data)):
            
        temp_log = ["\ngenoty "+data[row][0]+"|"]
            
        old_genoty = GenotypageManager.get_genotypage_by({"plaque":data[row][0],"position":data[row][1]})
                                     
        if len(old_genoty) != 0:
                
            old_genoty = old_genoty[0].to_array()
                
            for champ in range(1,len(data[row])):
                    
                temp = data[row][champ]
                    
                if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(temp)) is not None:
                    temp = str(temp[6:10]+"-"+temp[3:5]+"-"+temp[0:2])
                        
                if str(temp) != str(old_genoty[champ]):
                    temp_log.append(data[0][champ]+" : "+str(old_genoty[champ])+" to "+str(temp)+"|")
                        
        else:
            for champ in range(1,len(data[row])):
                temp_log.append(str(data[row][champ])+"|")
                    
        if len(temp_log) == 1:
            to_log_insert.append(["\nNone modif genotypage "+data[row][0]])
        else:
            to_log_insert.append(temp_log)    
               
        genoty_temp = Genotypage.create(data[row][0],data[row][1],data[row][2],data[row][3],data[row][4],data[row][5],data[row][6],data[row][7],data[row][8],data[row][9])
        GenotypageManager.register(genoty_temp) 
        
    return to_log_insert    
        
        
        
        