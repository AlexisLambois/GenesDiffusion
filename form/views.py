#! /usr/bin/python
#-*- coding:UTF8 -*-
from .manager.animalmanager import AnimalManager
from .manager.preleveurmanager import PreleveurManager 
from django.shortcuts import render
from django.conf import settings
import sys,os,csv
from django.core.files.storage import FileSystemStorage

def create_view(request):
    return render(request,'form/index.html',
        {
            'data_animal': AnimalManager.get_all_animals(),
        })

def insert_view(request):

    if request.method == 'POST' and request.FILES['myfile']:
        
        myfile = request.FILES['myfile']
        if extension_verif(myfile.name): 
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   
            data = data_gather( settings.BASE_DIR + uploaded_file_url)
            
            dictio = {}
            for row in range(0,len(data)):
                dictio.update({row:dara_row_verif(data[row])})
        else:
            uploaded_file_url = "mauvaise extension"
        return render(request, 'form/insert.html', {
            'uploaded_file_url': uploaded_file_url
        })           
    
    return render(request, 'form/insert.html')

def extension_verif(filename):
    tab = [".csv",".excel",".xlsx"]
    for extension in tab:      
        if extension == str(filename[filename.index('.'):]):
            return True
    return False

def data_gather(filename):
    mon_fichier = open(filename,"r")
    rep = []
    with mon_fichier as f:
        reader = csv.reader(f)
        for row in reader:
            line = row[0].split('\t')  
            rep.append(line)
    mon_fichier.close()
    return rep

def dara_row_verif(row):
    return None