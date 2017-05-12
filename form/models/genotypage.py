'''
Created on 12 mai 2017

@author: alexis
'''
from django.db import models

class Genotypage(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    plaque = models.CharField(max_length=25)
    position = models.CharField(max_length=3)
    format_puce = models.CharField(max_length=20)
    date_debut = models.DateField(null=True)
    date_scan = models.DateField(null=True)
    callrate = models.FloatField(null=True)
    link_to_file = models.CharField(max_length=4096,null=True)
    note = models.TextField(null=True)
    
    class Meta:
        unique_together = ('plaque','position')
        
    @classmethod
    def create(cls,plaque,position,format_puce,date_debut,date_scan,callrate,link_to_file,note):
        genotypage = cls(plaque = plaque,
            position = position,
            format_puce = format_puce,
            date_debut = date_debut,
            date_scan = date_scan,
            callrate = callrate,
            link_to_file = link_to_file,
            note = note
            )
        return genotypage
    
    #----------------------------------------------------------Getter/Setter----------------------------------------------------------#
    
    def get_id(self):
        return self.auto_increment_id
    
    def get_plaque(self):
        return self.plaque
    
    def get_position(self):
        return self.position
    
    def get_format_puce(self):
        return self.format_puce
    
    def get_date_debut(self):
        return self.date_debut
    
    def get_date_scan(self):
        return self.date_scan
    
    def get_callrate(self):
        return self.callrate
    
    def get_link_to_file(self):
        return self.link_to_file
    
    def get_note(self):
        return self.note
    
    #---------------------------------------------------------------------------------------------------------------------------#

    def set_plaque(self,plaque):
        self.plaque = plaque
        
    def set_position(self,position):
        self.position = position
        
    def set_format_puce(self,format_puce):
        self.format_puce = format_puce
        
    def set_date_debut(self,date_debut):
        self.date_debut = date_debut
        
    def set_date_scan(self,date_scan):
        self.date_scan = date_scan
        
    def set_callrate(self,callrate):
        self.callrate = callrate
        
    def set_link_to_file(self,link_to_file):
        self.link_to_file = link_to_file
        
    def set_note(self,note):
        self.note = note
        
    #----------------------------------------------------------Formatage affichage----------------------------------------------------------#
    
    def to_array(self):
        return[str(self.get_plaque()),str(self.get_position()),str(self.get_format_puce()),str(self.get_date_debut()),str(self.get_date_scan()),str(self.get_callrate()),str(self.get_link_to_file()),str(self.get_note())]
        
    def to_array_html(self):
        return[str(self.get_plaque()),str(self.get_position()),str(self.get_format_puce()),str(self.get_date_debut()),str(self.get_date_scan()),str(self.get_callrate()),str(self.get_link_to_file()),str(self.get_note())]
            