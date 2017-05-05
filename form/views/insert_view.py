'''
Created on 25 avr. 2017

@author: alexis
'''
from django.shortcuts import render
from django.conf import settings
import csv,re,json
from django.core.files.storage import FileSystemStorage
from ..manager.animalmanager import AnimalManager
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt
from pyexcel_ods import get_data
from openpyxl import load_workbook

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
            data_changed = find_data_changed(data)
            for row_number in range(1,len(data)-1):
                error_data.append(dara_row_verif(data[row_number]))
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
        data = (get_data(filename,start_column=0, column_limit=13)).values()[0]
        
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

def find_data_changed(data):
    id_data_changed = []
    for i in range(1,len(data)-1):
        
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

def dara_row_verif(row):   
    tab_validation = []
    if re.match(r"^[A-Z0-9]{9,20}$",str(row[0])) is None :  tab_validation.append(0)
    if re.match(r"^[A-Z]+[ \-']?[[A-Z]+[ \-']?]*[A-Z]+$",str(row[1])) is None :  tab_validation.append(1)
    if re.match(r"^[0-9]{1}$",str(row[2])) is None :  tab_validation.append(2)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",str(row[3])) is None :  tab_validation.append(3)
    if re.match(r"^[A-Z0-9]{9,20}$",str(row[4]))is None :  tab_validation.append(4)
    if re.match(r"^[A-Z0-9]{9,20}$",str(row[5]))is None :  tab_validation.append(5)
    if re.match(r"^[A-Z]{2}$",str(row[6]))is None :  tab_validation.append(6)
    if re.match(r"^(False|True)$",str(row[7]))is None :  tab_validation.append(7)
    return tab_validation

#----------------------------------------------------------Formatage affichage----------------------------------------------------------#
    
def to_html(data):
    if len(data) == 0:
        return format_html("<h1>Mauvaise Version de Fichier</h1>")
    else:
        text = "<table>"
        for animal in range(0,len(data)):
            text += "<tr id=" + str(animal) + ">"
            for data_animal in range(0,len(data[animal])):
                text += "<td class="+ str(data_animal) +">" + str(data[animal][data_animal]) + "</td>"
            text += "</tr>"
        text += "</table>"
        return format_html(text)