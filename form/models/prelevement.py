#! /usr/bin/python
#-*- coding:UTF8 -*-

from django.db import models
from form.models.animal import Animal
from form.manager.animalmanager import AnimalManager
from form.manager.preleveurmanager import PreleveurManager
from form.models.preleveur import Preleveur

class Prelevement(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    plaque = models.CharField(max_length=25)
    position = models.CharField(max_length=3)
    date_enregistrement = models.DateField(null=True)
    date_demande = models.DateField(null=True)
    date_extraction = models.DateField(null=True)
    date_reception_lille = models.DateField(null=True)
    type_materiel = models.CharField(max_length=20,null=True)
    dosage = models.FloatField(null=True)
    conformite_dosage =  models.NullBooleanField()
    code_barre = models.CharField(max_length=10,null=True)
    nombre_extraction = models.IntegerField(null=True)
    echec_extraction = models.CharField(max_length=255,null=True)
    statut_vcg = models.CharField(max_length=2,null=True)
    date_insertion = models.DateField(null=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    preleveur = models.ForeignKey(Preleveur, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('plaque','position')
    
    @classmethod
    def create(cls,plaque,position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,
               dosage,conformite_dosage,code_barre,nombre_extraction,echec_extraction,statut_vcg,date_insertion,animal,preleveur):
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
            echec_extraction = echec_extraction,
            statut_vcg = statut_vcg,
            date_insertion = date_insertion,
            animal = AnimalManager.get_animal_by_alpha({"numero":animal})[0],
            preleveur = PreleveurManager.get_preleveur_by_alpha({"numero":preleveur})[0]
            )
        return prelevement

    #----------------------------------------------------------Getter/Setter----------------------------------------------------------#
    
    def get_id(self):
        return self.auto_increment_id
    
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
    
    def get_date_insertion(self):
        return self.date_insertion
    
    def get_animal(self):
        return self.animal
    
    def get_preleveur(self):
        return self.preleveur
    
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
        
    def set_date_insertion(self,date_insertion):
        self.date_insertion = date_insertion
    
    def set_animal(self,animal):
        self.animal = animal
        
    def set_preleveur(self,preleveur):
        self.preleveur = preleveur
        
    #----------------------------------------------------------Formatage affichage----------------------------------------------------------#
    
    def to_array(self):
        return [str(self.get_plaque()),str(self.get_position()),str(self.get_date_enregistrement()),str(self.get_date_demande()),str(self.get_date_extraction()),str(self.get_date_reception_lille()),str(self.get_type_materiel()),str(self.get_dosage()),str(self.get_conformite_dosage()),str(self.get_code_barre()),str(self.get_nombre_extraction()),str(self.get_echec_extraction()),str(self.get_statut_vcg()),str(self.get_animal().get_numero()),str(self.get_preleveur().get_numero())]

    def to_string(self):
        return str(self.get_plaque())+"\t"+str(self.get_position())+"\t"+str(self.get_date_enregistrement())+"\t"+str(self.get_date_demande())+"\t"+str(self.date_extraction) \
            +"\t"+str(self.date_reception_lille)+"\t"+str(self.type_materiel)+"\t"+str(self.dosage)+"\t"+str(self.conformite_dosage)+"\t"+str(self.code_barre)+"\t" \
                +str(self.nombre_extraction)+"\t"+str(self.echec_extraction)+"\t"+str(self.statut_vcg)+"\t"+str(self.get_preleveur().to_string())+"\t"+str(self.get_animal().to_string())

    def to_array_html(self):
        return [str(self.get_date_insertion()),str(self.get_plaque()),str(self.get_position()),str(self.get_date_enregistrement()),str(self.get_date_demande()),str(self.get_date_extraction()),str(self.get_date_reception_lille()),str(self.get_type_materiel()),str(self.get_dosage()),str(self.get_conformite_dosage()),str(self.get_code_barre()),str(self.get_nombre_extraction()),str(self.get_echec_extraction()),str(self.get_statut_vcg())] + self.get_animal().to_array_html() + self.get_preleveur().to_array()

