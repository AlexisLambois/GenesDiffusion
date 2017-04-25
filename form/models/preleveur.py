import os, sys, string
from django.db import models

class Preleveur(models.Model):
    numeroagrement = models.CharField(max_length=20,primary_key=True)
    nom = models.CharField(max_length=255)
    
    def get_numeroagrement(self):
        return self.numeroagrement

    def get_nom(self):
        return self.nom

    def set_numeroagrement(self, numeroagrement):
        self.numeroagrement = numeroagrement

    def set_nom(self, nom):
        if nom.strip() == '':
            raise ValueError("Nom invalide")
        self.nom = nom

    def to_string(self):
        return str(self.numeroagrement)+"\t"+str(self.nom)
