from django.db import models
from django.utils.html import format_html

class Preleveur(models.Model):
    numero = models.CharField(max_length=20,primary_key=True)
    nom = models.CharField(max_length=255)
    
    @classmethod
    def create(cls,numero,nom):
        preleveur = cls(numero = numero,nom = nom)
        return preleveur  
    
    #----------------------------------------------------------Getter/Setter----------------------------------------------------------#
    
    def get_numero(self):
        return self.numero

    def get_nom(self):
        return self.nom
    
    #---------------------------------------------------------------------------------------------------------------------------#

    def set_numero(self, numero):
        self.numero = numero

    def set_nom(self, nom):
        if nom.strip() == '':
            raise ValueError("Nom invalide")
        self.nom = nom

    #----------------------------------------------------------Formatage affichage----------------------------------------------------------#
    
    def to_string(self):
        return str(self.get_numero())+"\t"+str(self.get_nom())
    
    def to_array(self):
        return [str(self.get_numero()),str(self.get_nom())]
    
    def to_html(self):
        text="<tr>"
        text+="<td class=\"preleveur\">"+str(self.get_numero())+"</td>"
        text+="<td class=\"preleveur\">"+str(self.get_nom())+"</td>"
        text+="</tr>"
        return format_html(text)
