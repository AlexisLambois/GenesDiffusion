'''
Created on 25 avr. 2017

@author: alexis
'''
from django.shortcuts import render
from django.conf import settings
import csv,re,json
from django.core.files.storage import FileSystemStorage
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt
from pyexcel_ods import get_data
from openpyxl import load_workbook
from form.manager.animalmanager import AnimalManager
from form.manager.cheptelmanager import CheptelManager
from form.manager.racemanager import RaceManager
from form.manager.preleveurmanager import PreleveurManager
from form.manager.prelevementmanager import PrelevementManager
from form.manager.genotypagemanager import GenotypageManager

@csrf_exempt
def insert_view(request):

    if request.method == 'POST' and request.FILES['myfile']:
        
        myfile = request.FILES['myfile']
        table = (request.POST.get('table'))
        error_data = []
        data = []
        if extension_verif(myfile.name): 
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
       
            data = data_gather( settings.BASE_DIR + uploaded_file_url)
            data.append([myfile.name])
            data.append([table])
            
            if table.lower() == "animal" and len(data[0]) == 10 :
                data_changed = find_data_changed_animal(data)
                for row_number in range(1,len(data)-2):
                    error_data.append(dara_row_verif_animal(data[row_number]))
            elif table.lower() == "prelevement" and len(data[0]) == 15:
                data_changed = find_data_changed_prelev(data)
                for row_number in range(1,len(data)-2):
                    error_data.append(dara_row_verif_prele(data[row_number]))
            elif table.lower() == "genotypage" and len(data[0]) == 10 :
                data_changed = find_data_changed_genoty(data)
                for row_number in range(1,len(data)-2):
                    error_data.append(dara_row_verif_genoty(data[row_number]))
            else:
                data = "<h3>Fichier incompatible avec le parametre " + str(table) + "</h3>"
                error_data = []
                data_changed = []  
        return render(request, 'form/insert.html', {
            'error_data' : error_data,
            'data' : json.dumps(data),
            'data_changed':json.dumps(data_changed)
        })           
    return render(request, 'form/insert.html')

#----------------------------------------------------------Fichier----------------------------------------------------------#

def extension_verif(filename):
    tab = [".csv",".ods",".xlsx",".xls"]
    for extension in tab:      
        if extension == str(filename[filename.index('.'):]):
            return True
    return False

def data_gather(filename):
    extension = str(filename[filename.index('.'):])
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

#----------------------------------------------------------Traitement----------------------------------------------------------#

def find_data_changed_prelev(data):
    id_data_changed = []
    for i in range(1,len(data)-2):
  
        if len(PrelevementManager.get_prelevement_by_alpha({"plaque":data[i][0],"position":data[i][1]})) != 0 :  
            old_prelevement = (PrelevementManager.get_prelevement_by_alpha({"plaque":data[i][0],"position":data[i][1]})[0]).to_array()
            temp = []
            
            for j in range(0,len(data[i])):
                split = data[i][j]
                if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[i][j])) is not None:
                    split = str(split[6:10]+"-"+split[3:5]+"-"+split[0:2])
                
                if str(split).upper() != str(old_prelevement[j]):
                    temp.append(j)
                    
            id_data_changed.append(temp)
    return id_data_changed

def find_data_changed_animal(data):
    id_data_changed = []
    for i in range(1,len(data)-2):
        
        if len(AnimalManager.get_animal_by_alpha({"numero":data[i][0]})) != 0 :  
            old_animal = (AnimalManager.get_animal_by_alpha({"numero":data[i][0]})[0]).to_array()
            temp = []
       
            for j in range(0,len(data[i])):
                split = data[i][j]
                
                if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[i][j])) is not None:
                    split = str(split[6:10]+"-"+split[3:5]+"-"+split[0:2])
               
                if str(split) != str(old_animal[j+2]):
                    temp.append(j)
                    
            id_data_changed.append(temp)
    return id_data_changed

def find_data_changed_genoty(data):
    id_data_changed = []
    for i in range(1,len(data)-2):

        if len(GenotypageManager.get_genotypage_by_beta({"plaque":data[i][0],"position":data[i][1]})) != 0 :  
            old_genotypage = (GenotypageManager.get_genotypage_by_beta({"plaque":data[i][0],"position":data[i][1]})[0]).to_array()
            temp = []
            
            for j in range(0,len(data[i])):
                split = data[i][j]
                if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(data[i][j])) is not None:
                    split = str(split[6:10]+"-"+split[3:5]+"-"+split[0:2])
                
                if str(split).upper() != str(old_genotypage[j]):
                    temp.append(j)
                    
            id_data_changed.append(temp)
    return id_data_changed


def dara_row_verif_animal(row):   
    tab_validation = []
    if re.match(r"^[A-Z0-9]{9,20}$",str(row[0])) is None :  tab_validation.append(0)
    if re.match(r"^[A-Z0-9]+([ ]*[-]*[A-Z0-9]*)*$",str(row[1])) is None :  tab_validation.append(1)
    if re.match(r"^[0-9]{1}$",str(row[2])) is None :  tab_validation.append(2)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[3])) is None :  tab_validation.append(3)
    if re.match(r"^[A-Z0-9]{5,20}$",str(row[4]))is None :  tab_validation.append(4)
    if re.match(r"^[A-Z0-9]{5,20}$",str(row[5]))is None :  tab_validation.append(5)
    if re.match(r"^[A-Z]{2}$",str(row[6]))is None :  tab_validation.append(6)
    if re.match(r"^(False|True)$",str(row[7]))is None :  tab_validation.append(7)
    if len(CheptelManager.get_cheptel_by_beta({"numero":row[8]})) == 0 : tab_validation.append(8)
    if len(RaceManager.get_race_by_beta({"numero":row[9]})) == 0 : tab_validation.append(9)
    return tab_validation

def dara_row_verif_prele(row):
    tab_validation = []
    if re.match(r"^[A-Z0-9]{7,23}[-]*[A-Z0-9]*$",str(row[0]).upper()) is None :  tab_validation.append(0)
    if re.match(r"^[A-Z0-9]{0,3}$",str(row[1]).upper()) is None :  tab_validation.append(1)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[2]).upper()) is None :  tab_validation.append(2)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[3]).upper()) is None :  tab_validation.append(3)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[4]).upper())is None :  tab_validation.append(4)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[5]).upper())is None :  tab_validation.append(5)
    if re.match(r"^[A-Z0-9]{0,20}$",str(row[6]).upper())is None :  tab_validation.append(6)
    if re.match(r"^[0-9]{1,3}\.?[0-9]{1,2}$",str(row[7]).upper())is None :  tab_validation.append(7)
    if re.match(r"^(False|True)$",str(row[8]))is None :  tab_validation.append(8)
    if re.match(r"^[A-Z0-9]{0,10}$",str(row[9]).upper())is None :  tab_validation.append(9)
    if re.match(r"^[0-9]*$",str(row[10]).upper())is None :  tab_validation.append(10)
    if re.match(r"^[A-Z0-9]*$",str(row[11]).upper())is None :  tab_validation.append(11)
    if re.match(r"^[0-9]{2}$",str(row[12]).upper())is None :  tab_validation.append(12)
    if len(AnimalManager.get_animal_by_beta({"numero":row[13]})) == 0 : tab_validation.append(13)
    if len(PreleveurManager.get_preleveur_by_beta({"numero":row[14]})) == 0 : tab_validation.append(14)
    return tab_validation

def dara_row_verif_genoty(row):
    tab_validation = []
    if re.match(r"^[A-Z0-9]{9,23}$",str(row[0]).upper()) is None :  tab_validation.append(0)
    if re.match(r"^[0-9]{0,3}$",str(row[1]).upper()) is None :  tab_validation.append(1)
    if re.match(r"^[A-Z0-9]{0,20}$",str(row[2]).upper()) is None :  tab_validation.append(2)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[3]).upper()) is None :  tab_validation.append(3)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[4]).upper())is None :  tab_validation.append(4)
    if re.match(r"^[0-9]{1,3}\.?[0-9]{1,2}$",str(row[5]).upper())is None :  tab_validation.append(5)
    if len(PrelevementManager.get_prelevement_by_beta({"plaque":row[8],"position":row[9]})) == 0 : 
        tab_validation.append(8)
        tab_validation.append(9)
    return tab_validation
    