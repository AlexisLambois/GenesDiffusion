'''
Created on 25 avr. 2017

@author: alexis
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import datetime
import csv,json
from ..manager.animalmanager import AnimalManager

@csrf_exempt
def update_view(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        data_changed = []
        if extension_verif(myfile.name): 
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   
            data = data_csv_gather( settings.BASE_DIR + uploaded_file_url)
            data.append([myfile.name])
            data_changed = find_data_changed(data)
            print(data_changed)
        return render(request, 'form/update.html', {'data' : json.dumps(data),'data_changed':json.dumps(data_changed)})      
    return render(request, 'form/update.html')

def find_data_changed(data):
    id_data_changed = []
    for id_animal in range (1,len(data)-1):
        temp = []
        old_animal = AnimalManager.get_animal_by_numero(data[id_animal][0])[0]
        for id in range(1,len(old_animal.to_array())):
            if str(data[id_animal][id]) != str(old_animal.to_array()[id]):temp.append(id)
        id_data_changed.append(temp)
    return id_data_changed

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