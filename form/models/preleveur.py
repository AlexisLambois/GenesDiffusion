import os, sys, string
from django.db import models

class Preleveur(models.Model):
    indentifier = models.CharField(max_length=20,primary_key=True)
    nom = models.CharField(max_length=255)
    
    def get_numero(self):
        return self.identifier

    def get_nom(self):
        return self.nom

    def set_numero(self, identifier):
        self.identifier = identifier

    def set_nom(self, nom):
        if nom.strip() == '':
            raise ValueError("Nom invalide")
        self.nom = nom

    def to_string(self):
        return str(self.numero)+"\t"+str(self.nom)
