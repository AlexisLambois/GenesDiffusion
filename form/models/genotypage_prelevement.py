'''
Created on 18 mai 2017

@author: alexis
'''
class Genotypage_Prelevement:
    
    def __init__(self,form_genotypage_plaque,form_genotypage_position,format_puce,date_debut,date_scan,callrate,link_to_file,note,form_prelevement_plaque,form_prelevement_position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,dosage,conformite_dosage,code_barre,nombre_extraction,echec_extraction,statut_vcg,date_insertion,animal_id,preleveur_id):
        self.form_genotypage_plaque = object_to_string(form_genotypage_plaque)
        self.form_genotypage_position = object_to_string(form_genotypage_position)
        self.format_puce = object_to_string(format_puce)
        self.date_debut = date_to_string(date_debut)
        self.date_scan = date_to_string(date_scan)
        self.callrate = object_to_string(callrate)
        self.link_to_file = object_to_string(link_to_file)
        self.note = object_to_string(note)
        self.form_prelevement_plaque = object_to_string(form_prelevement_plaque)
        self.form_prelevement_position = object_to_string(form_prelevement_position)
        self.date_enregistrement = date_to_string(date_enregistrement)
        self.date_demande = date_to_string(date_demande)
        self.date_extraction = date_to_string(date_extraction)
        self.date_reception_lille = date_to_string(date_reception_lille)
        self.type_materiel = object_to_string(type_materiel)
        self.dosage = object_to_string(dosage)
        self.conformite_dosage = object_to_string(conformite_dosage)
        self.code_barre = object_to_string(code_barre)
        self.nombre_extraction = object_to_string(nombre_extraction)
        self.echec_extraction = object_to_string(echec_extraction)
        self.statut_vcg = object_to_string(statut_vcg)
        self.date_insertion = date_to_string(date_insertion)
        self.animal_id = object_to_string(animal_id)
        self.preleveur_id = object_to_string(preleveur_id)
        
    def to_array(self): 
        return [self.form_genotypage_plaque,self.form_genotypage_position,self.format_puce,self.date_debut,self.date_scan,self.callrate,self.link_to_file,self.note,self.date_insertion,self.form_prelevement_plaque,self.form_prelevement_position,self.date_enregistrement,self.date_demande,self.date_extraction,self.date_reception_lille,self.type_materiel,self.dosage,self.conformite_dosage,self.code_barre,self.nombre_extraction,self.echec_extraction,self.statut_vcg,self.animal_id,self.preleveur_id]

def date_to_string(date):
    if date == None : 
        return "" 
    else : 
        return date.strftime('%d-%m-%Y')
    
def object_to_string(object):
    if object == None : 
        return "" 
    else : 
        return str(object)