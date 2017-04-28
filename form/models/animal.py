#! /usr/bin/python
#-*- coding:UTF8 -*-
from django.db import models
from .cheptel import Cheptel
from .race import Race
from ..manager.cheptelmanager import CheptelManager
from ..manager.racemanager import RaceManager
from django.utils.html import format_html

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
    date_insertion = models.DateField(null=True)
    ordre = models.CharField(max_length=3,null=True)
    
    @classmethod
    def create(cls,numero,nom,sexe,date_naissance,pere,mere,pays,jumeau,race,cheptel,ordre,date_insertion):
        animal = cls(numero = numero,
            nom = nom,
            sexe = sexe,
            date_naissance = date_naissance,
            pere = pere,
            mere = mere,
            jumeau = jumeau,
            pays = pays,
            cheptel = CheptelManager.get_cheptel_by_numero(cheptel)[0],
            race = RaceManager.get_race_by_numero(race)[0],
            ordre = ordre,
            date_insertion = date_insertion
            )
        return animal
        
    #----------------------------------------------------------Getter/Setter----------------------------------------------------------#
    
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
    
    def get_cheptel(self):
        return self.cheptel
    
    def get_race(self):
        return self.race      
    
    def get_ordre(self):
        return self.ordre
    
    def get_date_insertion(self):
        return self.date_insertion
    
    #---------------------------------------------------------------------------------------------------------------------------#
    
    def set_numero(self, numero):
        self.numero = numero
    
    def set_nom(self, nom):
        self.nom = nom
    
    def set_sexe(self, sexe):
        self.sexe = sexe
    
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
        
    def set_race(self, race):
        self.race = race
        
    def set_ordre(self, ordre):
        self.ordre=ordre
        
    def set_date_insertion(self, date_insertion):
        self.date_insertion=date_insertion
    
    #----------------------------------------------------------Formatage affichage----------------------------------------------------------#
    
    def to_array(self):
        return [self.get_numero(),self.get_nom(),self.get_sexe(),self.get_date_naissance(),self.get_pere(),self.get_mere(),self.get_pays(),self.get_jumeau()] + self.get_race().to_array() + self.get_cheptel().to_array()
        
    def to_string(self):
        return  (" Animal : "+self.get_numero()+"\t"+self.get_nom()+"\t"+self.get_sexe()+"\t"+str(self.get_date_naissance())+"\t"+self.get_pere()+"\t"+self.get_mere()+"\t"+str(self.get_jumeau())+"\t"+self.get_pays()+"\t"+self.cheptel.to_string()+"\t"+self.race.to_string()+"\t"+self.get_ordre()+"\t"+str(self.get_date_insertion())+"\n")    
    
    def to_html(self):
        text="<tr>"
        text+="<td class=\"animal\">"+str(self.get_ordre())+"</td>"
        text+="<td class=\"animal\">"+str(self.get_date_insertion())+"</td>"
        text+="<td class=\"animal\">"+self.get_numero()+"</td>"
        text+="<td class=\"animal\">"+self.get_nom()+"</td>"
        text+="<td class=\"animal\">"+self.get_sexe()+"</td>"
        text+="<td class=\"animal\">"+str(self.get_date_naissance())+"</td>"
        text+="<td class=\"animal\">"+self.get_pere()+"</td>"
        text+="<td class=\"animal\">"+self.get_mere()+"</td>"
        text+="<td class=\"animal\">"+self.get_pays()+"</td>"
        text+="<td class=\"animal\">"+str(self.get_jumeau())+"</td>"
        text+=self.get_race().to_html()
        text+=self.get_cheptel().to_html()
        text+="</tr>"
        return format_html(text)