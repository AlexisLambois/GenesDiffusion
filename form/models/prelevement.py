#! /usr/bin/python
#-*- coding:UTF8 -*-

import os, sys, string
from django.db import models
from django.utils.html import *
from .animal import Animal

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
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    @classmethod
    def create(cls,plaque,position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,
               dosage,conformite_dosage,code_barre,nombre_extraction,echec_extration,statut_vcg):
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
            animal = Animal.create("FR546456465","MUR",1,"2016-04-12","CASTOR","DE","FR",False))
        return prelevement

    def get_plaque(self):
        return self.plaque

    def get_position(self):
        return self.position

    def get_date_enregistrement(self):
        return self.date_enregistrement

    def get_date_demande(self):
        return self.date_demande

    def get_type_materiel(self):
        return self.type_materiel

    def get_date_extraction(self):
        return self.date_extraction

    def get_dosage(self):
        return self.dosage

    def get_conformite_dosage(self):
        return self.conformite_dosage

    def get_date_reception_lille(self):
        return self.date_reception_lille

    def get_code_barre(self):
        return self.code_barre

    def get_nombre_extraction(self):
        return self.nombre_extraction

    def get_echec_extraction(self):
        return self.echec_extraction

    def get_statut_vcg(self):
        return self.statut_vcg

    def set_plaque(self, plaque):
        self.plaque = plaque

    def set_position(self, position):
        self.position = position

    def set_date_enregistrement(self, date_enregistrement):
        self.date_enregistrement = date_enregistrement

    def set_date_demande(self, date_demande):
        self.date_demande = date_demande

    def set_type_materiel(self, type_materiel):
        self.type_materiel = type_materiel

    def set_date_extraction(self, date_extraction):
        self.date_extraction = date_extraction

    def set_dosage(self, dosage):
        self.dosage = dosage

    def set_conformite_dosage(self, conformite_dosage):
        self.conformite_dosage = conformite_dosage

    def set_date_reception_lille(self, date_reception_lille):
        self.date_reception_lille = date_reception_lille

    def set_code_barre(self, code_barre):
        self.code_barre = code_barre

    def set_nombre_extraction(self, nombre_extraction):
        self.nombre_extraction = nombre_extraction

    def set_echec_extraction(self, echec_extraction):
        self.echec_extraction = echec_extraction

    def set_statut_vcg(self, statut_vcg):
        self.statut_vcg = statut_vcg

    def to_string(self):
        return str(self.plaque)+"\t"+str(self.position)+"\t"+str(self.date_enregistrement)+"\t"+str(self.date_demande)+"\t"+str(self.type_materiel)+"\t" \
                       +str(self.date_extraction)+"\t"+str(self.dosage)+"\t"+str(self.conformite_dosage)+"\t"+str(self.date_reception_lille)+"\t"+str(self.code_barre)+"\t" \
                +str(self.nombre_extraction)+"\t"+str(self.echec_extraction)+"\t"+str(self.statut_vcg)

    def to_html(self):
        text = "<tr><td class=\"prelev\">"+self.plaque+"</td><td class=\"prelev\">"+self.position+"</td><td class=\"prelev\">"+self.date_enregistrement+"</td><td class=\"prelev\">"+self.date_demande+"</td><td class=\"prelev\">" \
            +self.date_extraction+"</td><td class=\"prelev\">"+self.date_reception_lille+"</td><td class=\"prelev\">"+self.type_materiel+"</td><td class=\"prelev\">"+self.dosage+"</td><td class=\"prelev\">" \
        +self.conformite_dosage+"</td><td class=\"prelev\">"+self.code_barre++"</td><td class=\"prelev\">"+self.echec_extration+"</td><td class=\"prelev\">"+self.nombre_extraction+"</td><td class=\"prelev\">"+self.statut_vcg+"</td></tr>"
        return format_html(text)
