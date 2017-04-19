
from django.db import models
import os, sys, string
from django.utils.html import *

class Cheptel(models.Model):
    numero = models.CharField(max_length=20,primary_key=True)
    detenteur = models.CharField(max_length=255,null=True)
    
    @classmethod
    def create(cls,numero,detenteur):
        cheptel = cls(numero = numero,
            detenteur = detenteur)
        return cheptel    

    def get_numero(self):
        return self.numero

    def get_detenteur(self):
        return self.detenteur

    def set_numero(self, numero):
        self.numero = numero

    def set_detenteur(self, detenteur):
        if detenteur.strip() == '':
            raise ValueError("Nom de detenteur invalide")
        self.detenteur = detenteur

    def to_string(self):
        return str(self.numero)+"\t"+str(self.detenteur)
    
    def to_html(self):
        text = "<td class=\"cheptel\">"+str(self.numero)+"</td><td class=\"cheptel\">"+str(self.detenteur)+"</td>"
        return format_html(text)    
        
    
