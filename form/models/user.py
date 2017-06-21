'''
Created on 19 juin 2017

@author: alexis
'''
#! /usr/bin/python
#-*- coding:UTF8 -*-
from django.db import models

class User(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    mdp = models.CharField(max_length=20)
    droit_insertion = models.NullBooleanField()
    
    @classmethod
    def create(cls,id,mdp,droit_insertion):
        user = cls(id = id,
            mdp =mdp,
            droit_insertion = droit_insertion
            )
        return user
        
    #----------------------------------------------------------Getter/Setter----------------------------------------------------------#
    
    def get_id(self):
        return self.id
    
    def get_mdp(self):
        return self.mdp
    
    def get_droit_insertion(self):
        return self.droit_insertion  
    
    #---------------------------------------------------------------------------------------------------------------------------#
    
    def set_id(self,id):
       self.id = id
    
    def set_mdp(self,mdp):
        self.mdp = mdp
        
    def set_droit_insertion(self,droit_insertion):
        self.droit_insertion = droit_insertion
    
  