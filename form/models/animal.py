#! /usr/bin/python
#-*- coding:UTF8 -*-
from django.db import models
from .cheptel import Cheptel
from .race import Race
import os, sys, string
from django.utils.html import *

class Animal(models.Model):
    numero = models.CharField(max_length=12,primary_key=True)
    nom = models.CharField(max_length=255,null=True)
    sexe = models.CharField(max_length=1,null=True)
    date_naissance = models.DateField(null=True)
    pere = models.CharField(max_length=12,null=True)    
    mere = models.CharField(max_length=12,null=True)     
    jumeau = models.NullBooleanField()
    pays = models.CharField(max_length=255,null=True)     
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    
    def get_numero(self):
        return self.numero
    
    def get_nom(self):
        return self.nom
    
    def get_sexe(self):
        return self.sexe
    
    def get_date_naissance(self):
        return self.date_naissance
    
    def get_pere(self):
        return self.pere
    
    def get_mere(self):
        return self.mere
    
    def get_jumeau(self):
        return self.jumeau
    
    def get_pays(self):
        return self.pays
    
    def get_race(self):
        return self.race    
    
    def get_cheptel(self):
        return self.cheptel
    
    def set_numero(self, numero):
        self.numero = numero
    
    def set_nom(self, nom):
        self.nom = nom
    
    def set_sexe(self, sexe):
        self.sexe = sexe
    
    def set_race(self, race):
        self.race = race
    
    def set_date_naissance(self, date_naissance):
        self.date_naissance = date_naissance
    
    def set_pere(self, pere):
        self.pere = pere
    
    def set_mere(self, mere):
        self.mere = mere
    
    def set_jumeau(self, jumeau):
        self.jumeau = jumeau
    
    def set_pays(self, pays):
        self.pays = pays
    
    def set_cheptel(self, cheptel):
        self.cheptel = cheptel
    
    def to_string(self):
        return str(self.numero)+"\t"+str(self.nom)+"\t"+str(self.sexe)+"\t"+str(self.race)+"\t"+str(self.date_naissance)+"\t"+str(self.pere)+"\t"+str(self.mere)+"\t"+str(self.jumeau)+"\t"+str(self.pays)+"\t"+str(self.cheptel)    
    
    def to_html(self):
        text = "<tr><td class=\"animal\">"+self.numero+"</td><td class=\"animal\">"+self.nom+"</td><td class=\"animal\">"+self.sexe+"</td><td class=\"animal\">"+str(self.date_naissance)+"</td><td class=\"animal\">"+self.pere+"</td><td class=\"animal\">"+self.mere+"</td><td class=\"animal\">"+self.pays+"</td><td class=\"animal\">"+str(self.jumeau)+"</td>"+self.race.to_html()+self.cheptel.to_html()+"</tr>"
        return format_html(text)