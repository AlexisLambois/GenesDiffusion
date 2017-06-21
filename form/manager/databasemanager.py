import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")
import psycopg2,re

class DatabaseManager(object):
	
	"""Cette classe permet de serialiser un objet en base de donnees
		ALPHA : Requete sur une valeur connue partiellement (ou entiere)
		BETA : Requete sur une valeur connue entierement
		GAMMA : Requete comportant une posibilite de sous requete
	"""

	pg_conn = None
	cursor = None

	@staticmethod
	def open_connexion():
		try:
			DatabaseManager.pg_conn = psycopg2.connect(dbname="bovin", user="admin", password="root", host="localhost")
			DatabaseManager.cursor = DatabaseManager.pg_conn.cursor()
		except Exception as e:
			print (e)
			sys.exit()

	@staticmethod
	def close_connexion():
		DatabaseManager.cursor.close()
		DatabaseManager.pg_conn.close()
	
	@staticmethod	
	def execute(requete):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	#----------------------------------------------------------PRELEVEURS----------------------------------------------------------#

	@staticmethod
	def select_all_preleveurs():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_preleveur;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_preleveur_by(tosql):
		if not tosql : return []
		DatabaseManager.open_connexion()
		requete = "SELECT * FROM form_preleveur WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-4]
		requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_preleveur_sous_requete(tosql):
		if not tosql : return ""
		requete = "(SELECT numero from form_preleveur WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-5]
		requete += ")"
		return requete

	@staticmethod
	def register_preleveur(numero, nom=''):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_preleveur(numero, nom) \
		VALUES('"+str(numero)+"', '"+str(nom)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', nom='"+str(nom)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()

	#----------------------------------------------------------RACES----------------------------------------------------------#
    
	@staticmethod
	def select_all_races():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_race;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_race_by(tosql):
		if not tosql : return []
		DatabaseManager.open_connexion()
		requete = "SELECT * FROM form_race WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-4]
		requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_race_sous_requete(tosql):
		if not tosql : return ""
		requete = "(SELECT numero from form_race WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-5]
		requete += ")"
		return requete
	
	@staticmethod
	def register_race(numero, nom=''):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_race(numero, nom) \
		VALUES('"+str(numero)+"', '"+str(nom)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', nom='"+str(nom)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()
		
	#----------------------------------------------------------CHEPTELS----------------------------------------------------------#

	@staticmethod
	def select_all_cheptels():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_cheptel;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_cheptel_by(tosql):
		if not tosql : return []
		DatabaseManager.open_connexion()
		requete = "SELECT * FROM form_cheptel WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-5]
		requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_cheptel_sous_requete(tosql):
		if not tosql : return ""
		requete = "(SELECT numero from form_cheptel WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-5]
		requete += ")"
		return requete

	@staticmethod
	def register_cheptel(numero, detenteur=''):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_cheptel(numero, detenteur) \
		VALUES('"+str(numero)+"', '"+str(detenteur)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', detenteur='"+str(detenteur)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()
		
	#----------------------------------------------------------ANIMALS----------------------------------------------------------#

	@staticmethod
	def select_all_animals():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_animal_by(tosql):
		if not tosql : return []
		DatabaseManager.open_connexion()
		requete = "SELECT * FROM form_animal WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-4]
		requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_animal_sous_requete(tosql,sous_requete):
		no_sous_requete = True
		requete = "(SELECT numero from form_animal WHERE "
		if tosql:
			for cle, valeur in tosql.items():
				requete += get_request_by_type(cle,valeur)
		for cle, valeur in sous_requete.items():
			if str(valeur) != "":
				no_sous_requete = False
				break
		if not tosql and no_sous_requete : return ""
		if not no_sous_requete :
			for cle, valeur in sous_requete.items():
				if str(valeur) != "":
					requete += get_request_by_type(cle,valeur)
		requete = requete[0:-5]
		requete += ")"
		return requete

	@staticmethod
	def register_animal(numero, nom, sexe, race, date_naissance, pere, mere, jumeau, pays, cheptel,ordre,date_insertion):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_animal(numero, nom, sexe, race_id, date_naissance, pere, mere, jumeau, pays, cheptel_id,ordre,date_insertion) \
		VALUES('"+str(numero)+"', '"+str(nom)+"', '"+str(sexe)+"', '"+str(race.get_numero())+"', \
		'"+str(date_naissance)+"', '"+str(pere)+"', '"+str(mere)+"', '"+str(jumeau)+"', '"+str(pays)+"', '"+str(cheptel.get_numero())+"', '"+str(ordre)+"', '"+str(date_insertion)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', nom='"+str(nom)+"', sexe='"+str(sexe)+"', race_id='"+str(race.get_numero())+"', \
		date_naissance='"+str(date_naissance)+"', pere='"+str(pere)+"', mere='"+str(mere)+"', \
		jumeau='"+str(jumeau)+"', pays='"+str(pays)+"', cheptel_id='"+str(cheptel.get_numero())+"', ordre='"+str(ordre)+"', date_insertion='"+str(date_insertion)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()
		
	#----------------------------------------------------------PRELEVEMENTS----------------------------------------------------------#

	@staticmethod
	def select_all_prelevements():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_prelevement;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_prelevement_by(tosql):
		if not tosql : return []
		DatabaseManager.open_connexion()
		requete = "SELECT * FROM form_prelevement WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-4]
		requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	
	@staticmethod
	def select_prelevement_sous_requete(tosql,sous_requete):
		no_sous_requete = True
		requete = "(SELECT auto_increment_id from form_prelevement WHERE "
		if tosql:
			for cle, valeur in tosql.items():
				requete += get_request_by_type(cle,valeur)
		for cle, valeur in sous_requete.items():
			if str(valeur) != "":
				no_sous_requete = False
				break
		if not tosql and no_sous_requete : return ""
		if not no_sous_requete :
			for cle, valeur in sous_requete.items():
				if str(valeur) != "":
					requete += get_request_by_type(cle,valeur)
		requete = requete[0:-5]
		requete += ")"
		return requete
	
	@staticmethod
	def select_prelevement_to_html(tab_id):
		DatabaseManager.open_connexion()
		if len(tab_id) == 0: 
			requete = "SELECT to_html from form_prelevement;"
		else:
			requete = "SELECT to_html from form_prelevement WHERE "
			for id in tab_id:
				requete += "auto_increment_id=" + str(id[0]) + " OR "
			requete = requete[0:-4]
			requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
		
	@staticmethod
	def register_prelevement(plaque,position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,dosage,conformite_dosage,code_barre,nombre_extraction,echec_extraction,statut_vcg,date_insertion,animal,preleveur,html):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_prelevement(plaque,position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,dosage,conformite_dosage,code_barre,nombre_extraction,echec_extraction,statut_vcg,date_insertion,animal_id,preleveur_id,to_html) \
		VALUES('"+str(plaque)+"', '"+str(position)+"', '"+str(date_enregistrement)+"', '"+str(date_demande)+"', '"+str(date_extraction)+"', '"+str(date_reception_lille)+"', '"+str(type_materiel)+"', '"+str(dosage)+"', '"+str(conformite_dosage)+"', '"+str(code_barre)+"', '"+str(nombre_extraction)+"', '"+str(echec_extraction)+"', '"+str(statut_vcg)+"', '"+str(date_insertion)+"', '"+str(animal.get_numero())+"', '"+str(preleveur.get_numero())+"', '"+str(html)+"') \
		ON CONFLICT(plaque,position) DO UPDATE \
		SET plaque='"+str(plaque)+"', position='"+str(position)+"', date_enregistrement='"+str(date_enregistrement)+"', date_demande='"+str(date_demande)+"', date_extraction='"+str(date_extraction)+"', date_reception_lille='"+str(date_reception_lille)+"', type_materiel='"+str(type_materiel)+"', dosage='"+str(dosage)+"', conformite_dosage='"+str(conformite_dosage)+"', code_barre='"+str(code_barre)+"', nombre_extraction='"+str(nombre_extraction)+"', echec_extraction='"+str(echec_extraction)+"', statut_vcg='"+str(statut_vcg)+"', date_insertion='"+str(date_insertion)+"', animal_id='"+str(animal.get_numero())+"', preleveur_id='"+str(preleveur.get_numero())+"', to_html='"+str(html)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()
		
	#----------------------------------------------------------GENOTYPAGES----------------------------------------------------------#

	@staticmethod
	def select_all_genotypages():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_genotypage;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_genotypage_by(tosql):
		if not tosql : return []
		DatabaseManager.open_connexion()
		requete = "SELECT * FROM form_genotypage WHERE "
		for cle, valeur in tosql.items():
			requete += get_request_by_type(cle,valeur)
		requete = requete[0:-4]
		requete += ";"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_genotypage_sous_requete(tosql,sous_requete):
		requete = "(SELECT numero from form_genotypage WHERE "
		for cle, valeur in tosql.items():
			requete += str(cle + "='" + str(valeur) + "' AND ")
		for cle, valeur in sous_requete.items():
			requete += str(cle + "=" + str(valeur) + " AND ")
		requete = requete[0:-5]
		requete += ")"
		no_sous_requete = True
		return requete

	@staticmethod
	def register_genotypage(plaque,position,format_puce,date_debut,date_scan,callrate,link_to_file,note,prelevement):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_genotypage (plaque,position,format_puce,date_debut,date_scan,callrate,link_to_file,note,prelevement_id) \
		VALUES('"+str(plaque)+"', '"+str(position)+"', '"+str(format_puce)+"', '"+str(date_debut)+"', '"+str(date_scan)+"', '"+str(callrate)+"', '"+str(link_to_file)+"', '"+str(note)+"', '"+str(prelevement.get_id())+"') \
		ON CONFLICT(plaque,position) DO UPDATE \
		SET plaque='"+str(plaque)+"', position='"+str(position)+"', format_puce='"+str(format_puce)+"', date_debut='"+str(date_debut)+"', date_scan='"+str(date_scan)+"', callrate='"+str(callrate)+"', link_to_file='"+str(link_to_file)+"', note='"+str(note)+"', prelevement_id='"+str(prelevement.get_id())+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()
	
	#----------------------------------------------------------FUSION GENOTYPAGE PRELEVEMENT----------------------------------------------------------#
	
	@staticmethod
	def fusion():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("select form_genotypage.plaque,form_genotypage.position,format_puce,date_debut,date_scan,callrate,link_to_file,note,form_prelevement.plaque,form_prelevement.position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,dosage,conformite_dosage,code_barre,nombre_extraction,echec_extraction,statut_vcg,date_insertion,animal_id,preleveur_id from form_genotypage RIGHT JOIN form_prelevement ON form_prelevement.auto_increment_id = form_genotypage.prelevement_id ORDER BY form_prelevement.auto_increment_id ASC;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def get_fusion_by(tosql_genotype,tosql_prelevement):
		DatabaseManager.open_connexion()
		requete = "select form_genotypage.plaque,form_genotypage.position,format_puce,date_debut,date_scan,callrate,link_to_file,note,e1.plaque,e1.position,date_enregistrement,date_demande,date_extraction,date_reception_lille,type_materiel,dosage,conformite_dosage,code_barre,nombre_extraction,echec_extraction,statut_vcg,date_insertion,animal_id,preleveur_id from form_genotypage RIGHT JOIN "
		if not tosql_prelevement : 
			requete += " form_prelevement AS e1 "
		else:
			requete += " (SELECT * FROM form_prelevement WHERE "
			for cle, valeur in tosql_prelevement.items():
				requete += get_request_by_type(cle,valeur)
			requete = requete[0:-4]
			requete += ") AS e1 "
		requete += "ON e1.auto_increment_id = form_genotypage.prelevement_id "
		for cle, valeur in tosql_genotype.items():
			requete += "AND "
			requete += get_request_by_type(cle,valeur)
			requete = requete[0:-4]
		requete += "ORDER BY e1.auto_increment_id ASC;"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	#----------------------------------------------------------User----------------------------------------------------------#
	@staticmethod
	def select_user(id):
		DatabaseManager.open_connexion()
		requete = "SELECT * from form_user WHERE id='"+id+"';"
		DatabaseManager.cursor.execute(requete)
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def register_user(id,mdp,droit_insertion):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_user (id,mdp,droit_insertion) \
		VALUES('"+str(id)+"', '"+str(mdp)+"', '"+str(droit_insertion)+"') \
		ON CONFLICT(id) DO UPDATE \
		SET id='"+str(id)+"', mdp='"+str(mdp)+"', droit_insertion='"+str(droit_insertion)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()
	
def get_request_by_type(cle,valeur):
	if str(valeur)[0] == "=" or str(valeur)[0] == "<" or str(valeur)[0] == ">":
		return str(cle + str(valeur) + " AND ")
	elif (re.match(r"^(FALSE|TRUE)$",str(valeur))is not None) or (re.match(r"^([0-9]+)$",str(valeur))is not None) or (re.match(r"^([0-9]+.[0-9]+)$",str(valeur))is not None):
		return str(cle + "='" + str(valeur) + "' AND ")
	elif valeur[0] == "(":
		return str(cle +" IN "+ str(valeur) + " AND ")
	else:
		return str(cle + " LIKE '" + str(valeur) + "%' AND ")
	return ""
