#! /usr/bin/python
#-*- coding:UTF8 -*-

from django.db import models
from .animal import Animal
from form.manager.animalmanager import AnimalManager
from form.manager.preleveurmanager import PreleveurManager
from django.utils.html import format_html
from form.models.preleveur import Preleveur

class Prelevement(models.Model):
    plaque = models.CharField(max_length=25,primary_key=True)
    position = models.CharField(max_length=3,primary_key = True)
    date_enregistrement = models.DateField(null=True)
    date_demande = models.DateField(null=True)
    date_extraction = models.DateField(null=True)
    date_reception_lille = models.DateField(null=True)
    type_materiel = models.CharField(max_length=20,null=True)
    dosage = models.FloatField(null=True)
    conformite_dosage = models.NullBooleanField()
    code_barre = models.CharField(max_length=10,null=True)
    nombre_extraction = models.IntegerField(null=True)
    echec_extration = models.CharField(max_length=255,null=True)
    statut_vcg = models.CharField(max_length=2,null=True)
    preleveur = models.ForeignKey(Preleveur, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    @classmethod
    def create(cls,plaque,position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,
               dosage,conformite_dosage,code_barre,nombre_extraction,echec_extration,statut_vcg,preleveur,animal):
        prelevement = cls(plaque = plaque,
            position = position,
            date_enregistrement = date_enregistrement,
            date_demande = date_demande,
            date_extraction = date_extraction,
            date_reception_lille = date_reception_lille,
            type_materiel = type_materiel,
            dosage = dosage,
            conformite_dosage = conformite_dosage,
            code_barre = code_barre,
            nombre_extraction = nombre_extraction,
            echec_extration = echec_extration,
            statut_vcg = statut_vcg,
            preleveur = PreleveurManager.get_preleveur_by_alpha({"numero":preleveur})[0],
            animal = AnimalManager.get_animal_by_alpha({"numero":animal})[0]
            )
        return prelevement

    #----------------------------------------------------------Getter/Setter----------------------------------------------------------#
    
    def get_plaque(self):
        return self.plaque

    def get_position(self):
        return self.position

    def get_date_enregistrement(self):
        return self.date_enregistrement

    def get_date_demande(self):
        return self.date_demande
    
    def get_date_extraction(self):
        return self.date_extraction
    
    def get_date_reception_lille(self):
        return self.date_reception_lille

    def get_type_materiel(self):
        return self.type_materiel

    def get_dosage(self):
        return self.dosage

    def get_conformite_dosage(self):
        return self.conformite_dosage

    def get_code_barre(self):
        return self.code_barre

    def get_nombre_extraction(self):
        return self.nombre_extraction

    def get_echec_extraction(self):
        return self.echec_extraction

    def get_statut_vcg(self):
        return self.statut_vcg
    
    def get_preleveur(self):
        return self.preleveur
    
    def get_animal(self):
        return self.animal
    
    #---------------------------------------------------------------------------------------------------------------------------#

    def set_plaque(self, plaque):
        self.plaque = plaque

    def set_position(self, position):
        self.position = position

    def set_date_enregistrement(self, date_enregistrement):
        self.date_enregistrement = date_enregistrement

    def set_date_demande(self, date_demande):
        self.date_demande = date_demande
        
    def set_date_extraction(self, date_extraction):
        self.date_extraction = date_extraction
        
    def set_date_reception_lille(self, date_reception_lille):
        self.date_reception_lille = date_reception_lille

    def set_type_materiel(self, type_materiel):
        self.type_materiel = type_materiel

    def set_dosage(self, dosage):
        self.dosage = dosage

    def set_conformite_dosage(self, conformite_dosage):
        self.conformite_dosage = conformite_dosage

    def set_code_barre(self, code_barre):
        self.code_barre = code_barre

    def set_nombre_extraction(self, nombre_extraction):
        self.nombre_extraction = nombre_extraction

    def set_echec_extraction(self, echec_extraction):
        self.echec_extraction = echec_extraction

    def set_statut_vcg(self, statut_vcg):
        self.statut_vcg = statut_vcg
        
    def set_preleveur(self,preleveur):
        self.preleveur = preleveur
    
    def set_animal(self,animal):
        self.animal = animal
        
    #----------------------------------------------------------Formatage affichage----------------------------------------------------------#
    
    def to_array(self):
        return [str(self.get_plaque()),str(self.get_position()),str(self.get_date_enregistrement()),str(self.get_date_demande()),str(self.get_date_extraction()),str(self.get_date_reception_lille()),str(self.get_type_materiel()),str(self.get_dosage()),str(self.get_conformite_dosage()),str(self.get_code_barre()),str(self.get_nombre_extraction()),str(self.get_echec_extraction()),str(self.get_statut_vcg())] + self.get_preleveur().to_array() + self.get_animal().to_array()

    def to_string(self):
        return str(self.get_plaque())+"\t"+str(self.get_position())+"\t"+str(self.get_date_enregistrement())+"\t"+str(self.get_date_demande())+"\t"+str(self.date_extraction) \
            +"\t"+str(self.date_reception_lille)+"\t"+str(self.type_materiel)+"\t"+str(self.dosage)+"\t"+str(self.conformite_dosage)+"\t"+str(self.code_barre)+"\t" \
                +str(self.nombre_extraction)+"\t"+str(self.echec_extraction)+"\t"+str(self.statut_vcg)+"\t"+str(self.get_preleveur().to_string())+"\t"+str(self.get_animal().to_string())

    def to_html(self):
        text="<tr>"
        text+="<td class=\"prelevement\">"+str(self.get_plaque())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_position())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_date_enregistrement())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_date_demande())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_date_extraction())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_date_reception_lille())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_type_materiel())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_dosage())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_conformite_dosage())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_code_barre())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_nombre_extraction())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_echec_extraction())+"</td>"
        text+="<td class=\"prelevement\">"+str(self.get_statut_vcg())+"</td>"
        text+=str(self.get_preleveur().to_html())
        text+=str(self.get_animal().to_html())
        text+="</tr>"
        return format_html(text)
