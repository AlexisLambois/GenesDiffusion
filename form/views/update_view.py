'''
Created on 25 avr. 2017

@author: alexis
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import csv,json

@csrf_exempt
def update_view(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if extension_verif(myfile.name): 
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   
            data = data_csv_gather( settings.BASE_DIR + uploaded_file_url)
            data.append([myfile.name]) 
        return render(request, 'form/update.html', {'data' : json.dumps(data)})      
    return render(request, 'form/update.html')

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