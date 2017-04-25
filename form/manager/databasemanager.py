import os, sys, string

sys.path.append("/usr/local/lib/python2.7/dist-packages")

import psycopg2

class DatabaseManager(object):
	"""Cette classe permet de serialiser un objet en base de donnees"""

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
	def select_all_preleveurs():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM preleveur;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_preleveur_by_numero(numero):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM preleveur WHERE numero='"+str(numero)+"';")
		data = DatabaseManager.cursor.fetchone()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_preleveurs_by_nom(nom):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM preleveur WHERE nom='"+str(nom)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def register_preleveur(numero, nom=''):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO preleveur(numero, nom) \
		VALUES('"+str(numero)+"', '"+str(nom)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', nom='"+str(nom)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()

	@staticmethod
	def select_all_races():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_race;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_race_by_numero(numero):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_race WHERE numero='"+str(numero)+"';")
		data = DatabaseManager.cursor.fetchone()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_race_by_nom(nom):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_race WHERE nom='"+str(nom)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def register_race(numero, nom=''):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_race(numero, nom) \
		VALUES('"+str(numero)+"', '"+str(nom)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', nom='"+str(nom)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()

	@staticmethod
	def select_all_cheptels():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_cheptel;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_cheptel_by_numero(numero):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_cheptel WHERE numero='"+str(numero)+"';")
		data = DatabaseManager.cursor.fetchone()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_cheptel_by_detenteur(detenteur):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_cheptel WHERE detenteur='"+str(detenteur)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def register_cheptel(numero, detenteur=''):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("INSERT INTO form_cheptel(numero, detenteur) \
		VALUES('"+str(numero)+"', '"+str(detenteur)+"') \
		ON CONFLICT(numero) DO UPDATE \
		SET numero='"+str(numero)+"', detenteur='"+str(detenteur)+"';")
		DatabaseManager.pg_conn.commit()
		DatabaseManager.close_connexion()

	@staticmethod
	def select_all_animals():
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal;")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_animal_by_numero(numero):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE numero='"+str(numero)+"';")
		data = DatabaseManager.cursor.fetchone()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_animal_by_nom(nom):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE nom='"+str(nom)+"';")
		data = DatabaseManager.cursor.fetchone()
		DatabaseManager.close_connexion()
		return data	
		
	@staticmethod
	def select_animals_by_sexe(sexe):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE sexe='"+str(sexe)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
		
	@staticmethod
	def select_animals_by_date_naissance(date_naissance):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE date_naissance='"+str(date_naissance)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_animals_by_pere(pere):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE pere='"+str(pere)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_animals_by_mere(mere):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE mere='"+str(mere)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_animals_by_pays(pays):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE pays='"+str(pays)+"'")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_animals_by_race(race):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE race_id='"+str(race)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

	@staticmethod
	def select_animals_by_cheptel(cheptel):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE cheptel_id='"+str(cheptel)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_animals_by_ordre(ordre):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE ordre='"+str(ordre)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data
	
	@staticmethod
	def select_animals_by_date_insertion(date_insertion):
		DatabaseManager.open_connexion()
		DatabaseManager.cursor.execute("SELECT * FROM form_animal WHERE date_insertion='"+str(date_insertion)+"';")
		data = DatabaseManager.cursor.fetchall()
		DatabaseManager.close_connexion()
		return data

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
