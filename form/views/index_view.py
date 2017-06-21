'''
Created on 24 mai 2017

@author: alexis
'''
from django.shortcuts import render
from form.manager.usermanager import UserManager
import json

def index_view(request):
    
    """ Test si on a un envoi du formulaire """
    
    if request.method == 'POST':
        
        """ Recuperation de id utilisateur et de son mot de passe """
        
        id = (request.POST.get('id'))
        pwd = (request.POST.get('pwd'))
        user_temp = UserManager.get_user(id) #On va chercher l utilisateur correspondant
        
        """ Test si un utilisateur correspont et si c est le bon mot de passe """
        
        if user_temp is not None and pwd == user_temp.get_mdp():
            
            """ On retourne l id utilisateur et les droits qui lui sont lies """
            
            data = [user_temp.get_id(),user_temp.get_droit_insertion()]
            
            return render(request,'form/index.html',{'data': json.dumps(data)})
        
    return render(request,'form/index.html',{})