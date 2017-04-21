#! /usr/bin/python
#-*- coding:UTF8 -*-
from .manager.animalmanager import AnimalManager
from .manager.preleveurmanager import PreleveurManager 
from django.shortcuts import render
from django.conf import settings
import sys,os,csv,re
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template import loader
from django.utils.html import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_view(request):
    return render(request,'form/index.html',
        {
            'data_animal': AnimalManager.get_all_animals(),
        })

@csrf_exempt
def insert_view(request):

    if request.method == 'POST' and request.FILES['myfile']:
        
        myfile = request.FILES['myfile']
        error_data = []
        data = []
        if extension_verif(myfile.name): 
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   
            data = data_csv_gather( settings.BASE_DIR + uploaded_file_url)
            
           
            for row_number in range(0,len(data)):
                error_data.append(dara_row_verif(data[row_number]))
           
        return render(request, 'form/insert.html', {
            'data_html': to_html(data),
            'error_data' : error_data,
            'data' : data
        })           
    
    return render(request, 'form/insert.html')

def extension_verif(filename):
    tab = [".csv",".excel",".xlsx"]
    for extension in tab:      
        if extension == str(filename[filename.index('.'):]):
            return True
    return False

def data_csv_gather(filename):
    mon_fichier = open(filename,"r")
    data = []
    with mon_fichier as f:
        reader = csv.reader(f)
        for row in reader: 
            data.append(row[0].split('\t'))
    mon_fichier.close()
    return data

def dara_row_verif(row):   
    tab_validation = []
    if re.match(r"^[A-Z0-9]{9,20}$",row[0]) is None :  tab_validation.append(0)
    if re.match(r"^[A-Z]+[ \-']?[[A-Z]+[ \-']?]*[A-Z]+$",row[1]) is None :  tab_validation.append(1)
    if re.match(r"^[0-9]{1}$",row[2]) is None :  tab_validation.append(2)
    if re.match(r"^(0?\d|[12]\d|3[01])/(0?\d|1[012])/((?:19|20)\d{2})$",row[3]) is None :  tab_validation.append(3)
    if re.match(r"^[A-Z0-9]{9,20}$",row[4])is None :  tab_validation.append(4)
    if re.match(r"^[A-Z0-9]{9,20}$",row[5])is None :  tab_validation.append(5)
    if re.match(r"^[A-Z]{2}$",row[6])is None :  tab_validation.append(6)
    if re.match(r"^(False|True)$",row[7])is None :  tab_validation.append(7)
    return tab_validation

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
    