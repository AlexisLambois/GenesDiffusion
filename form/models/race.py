import os, sys, string
from django.db import models
from django.utils.html import *

class Race(models.Model):
    numero = models.CharField(max_length=20,primary_key=True)
    nom = models.CharField(max_length=255,null=True)        

    def get_numero(self):
        return self.numero

    def get_nom(self):
        return self.nom

    def set_numero(self, numero):
        self.numero = numero

    def set_nom(self, nom):
        if nom.strip() == '':
            raise ValueError("Nom invalide")
        self.nom = nom

    def to_string(self):
        return str(self.numero)+"\t"+str(self.nom)

    def to_html(self):
        text = "<td class=\"race\">"+str(self.numero)+"</td><td class=\"race\">"+str(self.nom)+"</td>"
        return format_html(text)    