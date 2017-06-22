var created_infos_genotypage = false;
var created_infos_prelevement = false;

/* Action bouton generation affichage exportation 
 * Cf genotypage.html
 * Genere l affichage d export de genotypage.html
 */

function open_infos_genotypage(){
	
	// On fait disparaitre le tableau et on affiche la div de sauvegarde
	
	document.getElementsByClassName('container')[0].hidden = true;
	document.getElementsByClassName('infos')[0].hidden = false;
	
	// Si c'est la premiere fois on genere les cases et leurs labels 
	
	if (!created_infos_genotypage) {
		document.getElementById('check').checked = false;
		text = "<table>";
		text += "<th>Genotyapge</th>";
		for (var i = 0; i < genotypage.length; i++) {
			text += "<tr><td><label>" + genotypage[i] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "<th>Prelevement</th>";
		for (var i = genotypage.length; i < prelevement.length+genotypage.length; i++) {
			text += "<tr><td><label>" + prelevement[i-genotypage.length] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "<tr><td><label>Animal</label><input type=\"checkbox\"value=\"22\"></td></tr>";
		text += "<tr><td><label>Preleveur</label><input type=\"checkbox\"value=\"23\"></td></tr>";
		text += "</table>",
		$(text).appendTo(".form");
		created_infos_genotypage = true;
	}
	
}

/* Action bouton generation affichage exportation 
 * Cf print.html
 * Genere l affichage d export de print.html
 */

function open_infos_prelevement(){
	
	// On fait disparaitre le tableau et on affiche la div de sauvegarde
	
	document.getElementsByClassName('container')[0].hidden = true;
	document.getElementsByClassName('infos')[0].hidden = false;
	
	// Si c'est la premiere fois on genere les cases et leurs labels 
	
	if (!created_infos_prelevement) {
		document.getElementById('check').checked = false;
		text = "<table>";
		text += "<th>Prelevement</th>";
		for (var i = 0; i < prelevement.length; i++) {
			text += "<tr><td><label>" + prelevement[i] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "<th>Animal</th>";
		for (var i = prelevement.length; i < animal.length+prelevement.length; i++) {
			text += "<tr><td><label>" + animal[i-prelevement.length] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "<th>Cheptel</th>";
		for (var i = prelevement.length+animal.length; i < animal.length+prelevement.length+cheptel.length; i++) {
			text += "<tr><td><label>" + cheptel[i-(prelevement.length+animal.length)] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "<th>Race</th>";
		for (var i = prelevement.length+animal.length+cheptel.length; i < animal.length+prelevement.length+cheptel.length+race.length; i++) {
			text += "<tr><td><label>" + race[i-(prelevement.length+animal.length+cheptel.length)] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "<th>Preleveur</th>";
		for (var i = prelevement.length+animal.length+cheptel.length+race.length; i < animal.length+prelevement.length+cheptel.length+race.length+preleveur.length; i++) {
			text += "<tr><td><label>" + preleveur[i-(prelevement.length+animal.length+cheptel.length+race.length)] + "</label><input type=\"checkbox\"value=\"" + i + "\"></td></tr>";
		}
		text += "</table>",
		$(text).appendTo(".form");
		created_infos_prelevement = true;
	}
}

/* Requete permettant le retour des donnees correspondant a la recherche
 * @params :
 * 	indice = tableau contenant les indices des colonnnes ou il y a eu une saisie
 * 	inputs = tableau contenant toutes les entrees dans les zones de saisie
 * 	operateurs = tableau contenant les operateurs ( >,=,< ) ou rien selon l indice des colonnes 
 * Cf print.html
 */

function getData(indice,inputs,operateurs){
	
	// Requete POST appelle printer.py
	
	$.ajax({
		type: "POST",
		url: "/ajax/printer/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs},
		success: function(data) {
			affiche_tab(data,"#data");
		}
	});
};

/* Requete permettant le retour des donnees correspondant a la recherche
 * @params :
 * 	indice = tableau contenant les indices des colonnnes ou il y a eu une saisie
 * 	inputs = tableau contenant toutes les entrees dans les zones de saisie
 * 	operateurs = tableau contenant les operateurs ( >,=,< ) ou rien selon l indice des colonnes 
 * Cf genotypage.html
 */

function getGenotypage(indice,inputs,operateurs){
	
	// Requete GET appelle genoty.py
	
	$.ajax({
		type: "GET",
		url: "/ajax/genoty/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs},
		success: function(data) {
			affiche_tab(data,"#data");
		}
	});
};

/* Requete permettant l insertion de donnees en base 
 * @params :
 *	data = tableau double dimension contenant les donnees a inserer 
 * Cf insert.html
 */

function insertAnimal(data){

	// Requete POST appelle insert.py

	$.ajax({
		type: "POST",
		url: "/ajax/add/",
		data: {'data':data},
		success: function(data) {
			document.getElementsByClassName('data_tab')[0].innerHTML = "";
			document.getElementsByClassName('access')[0].innerHTML = "";		
			$("<h3>Les logs sont disponibles : " + data + "</h3>").appendTo(".access");
		}
	});
};

/* Action declencher par le bouton export de l affichage save
 * @params :
 *	indice = tableau contenant les indices des colonnnes ou il y a eu une saisie
 * 	inputs = tableau contenant toutes les entrees dans les zones de saisie
 * 	operateurs = tableau contenant les operateurs ( >,=,< ) ou rien selon l indice des colonnes 
 * 	case_cocher = tableau contenant les indices des colonnnes souhaiter dans le tableur final
 * Cf print.html
 */

function saveData(indice,inputs,operateurs,case_cocher){
	
	// Requete POST appelle print.py

	$.ajax({
		type: "POST",
		url: "/ajax/save/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs,'case_cocher':case_cocher},
		success: function(data) {
			
			// Retour a l affichage du tableau
			
			document.getElementsByClassName('container')[0].hidden = false;
			document.getElementsByClassName('infos')[0].hidden = true;
		}
	});
};

/* Action declencher par le bouton export de l affichage save
 * @params :
 *	indice = tableau contenant les indices des colonnnes ou il y a eu une saisie
 * 	inputs = tableau contenant toutes les entrees dans les zones de saisie
 * 	operateurs = tableau contenant les operateurs ( >,=,< ) ou rien selon l indice des colonnes 
 * 	case_cocher = tableau contenant les indices des colonnnes souhaiter dans le tableur final
 * Cf genotypage.html
 */

function saveData_Genoty(indice,inputs,operateurs,case_cocher){
	
	// Requete POST appelle genoty.py

	$.ajax({
		type: "POST",
		url: "/ajax/save_geno/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs,'case_cocher':case_cocher},
		success: function(data) {
			
			// Retour a l affichage du tableau
			
			document.getElementsByClassName('container')[0].hidden = false;
			document.getElementsByClassName('infos')[0].hidden = true;
		}
	});
};

/* Recherche automatique a chaque saisie dans les champs
 * @params :
 *	table = nom de la table questionner ( race/cheptel/preleveur )
 * 	input = saisie du champ id
 * 	insert = boolean true : saisie pour insert / false : saisie pour update 
 * Cf admin.html
 */

function findData(table,input_id,insert){
	
	// Requete POST appelle genoty.py

	$.ajax({
		type: "POST",
		url: "/ajax/find/",
		data: {'table': table,'input_id':input_id},
		success: function(data) {
			if(sessionStorage.getItem('droit')){
				if (!insert){
					document.getElementsByClassName(table+"_contenu")[0].innerHTML = "";
					if( data == "Null"){
						$("<h2 style=\"color:red\" >Aucune correspondance</h2>").appendTo("."+table+"_contenu");
					}else if( data != "None" ){
						$("<input type=\"text\" name=\"attribut\" value=\"" + data + "\"\>").appendTo("."+table+"_contenu");
						$("<input type=\"submit\" value=\"Update\">").appendTo("."+table+"_contenu");
					}
				}else{
					document.getElementsByClassName(table+"_contenu")[1].innerHTML = "";
					if( data == "Null"){
						$("<input type=\"submit\" value=\"Insérez-le\">").appendTo("."+table+"_contenu");
					}else if( data != "None" ){
						$("<h2 style=\"color:red\" >Id déjà existant</h2>").appendTo("."+table+"_contenu");
					}
				}
			}else{
				document.location.href="/";
			}	
		}
	});
};

//------------------------------------Mise au propre Affichage--------------------------------------------//

show = [true,true,true,true,true];

var genotypage = ["Plaque","Position","Format de puce","Date de Debut","Date de Scan","CallRate","Link to File","Note"];
var prelevement = ["Date Insertion","Plaque","Position","Date Enregistrement","Date Demande","Date Extraction","Date Reception Lille","Type de Materiel","Dosage","Conformite","Code Barre","Nombre Extraction","Echec Extraction","Statut VCG"];
var preleveur = ["Numero Agrement","Nom"];
var animal = ["Ordre","Date Insert/Up","Id","Nom","Sexe","Date de naissance","Pere","Mere","Pays","Jumeaux"];
var race = ["Numero Race","Nom Race"];
var cheptel = ["Cheptel Actuel","Detenteur Actuel"];

function affiche_entete(nom_entete){
	var text = "";
	if(nom_entete == "prelevement" ){
		for (var i = 0; i < prelevement.length; i++) {
			text += "<td class=\"prelevement\">" + prelevement[i] + "</td>";
		}
	}else if( nom_entete == "genotypage" ){
		for (var i = 0; i < genotypage.length; i++) {
			text += "<td class=\"genotypage\">" + genotypage[i] + "</td>";
		}
	}else if( nom_entete == "animal" ){
		for (var i = 0; i < animal.length; i++) {
			text += "<td class=\"animal\">" + animal[i] + "</td>";
		}
	}else if( nom_entete == "cheptel" ){
		for (var i = 0; i < cheptel.length; i++) {
			text += "<td class=\"cheptel\">" + cheptel[i] + "</td>";
		}
	}else if( nom_entete == "race" ){
		for (var i = 0; i < race.length; i++) {
			text += "<td class=\"race\">" + race[i] + "</td>";
		}
	}
	return text;
}

function swap(integer){
	if(show[integer]){
		show[integer]=false;
	}else{
		show[integer]=true;
	}
	show_hide("prelevement",show[0]);
	show_hide("preleveur",show[1]);
	show_hide("animal",show[2]);
	show_hide("cheptel",show[3]);
	show_hide("race",show[4]);
}

function genere_x_text(int,insert){
	var text = "";
	for(var i=0; i<int; i++){
		text += insert;
	}
	return text;
}

function genere_champs_affichage(){
	
	var text = "";
	for (var i = 0; i < prelevement.length; i++) {
		text += "<td class=\"prelevement\">" + prelevement[i] + "</td>";
	}
	for (var i = 0; i < animal.length; i++) {
		text += "<td class=\"animal\">" + animal[i] + "</td>";
	}
	for (var i = 0; i < cheptel.length; i++) {
		text += "<td class=\"cheptel\">" + cheptel[i] + "</td>";
	}
	for (var i = 0; i < race.length; i++) {
		text += "<td class=\"race\">" + race[i] + "</td>";
	}
	for (var i = 0; i < preleveur.length; i++) {
		text += "<td class=\"preleveur\">" + preleveur[i] + "</td>";
	}
	return text;
}

function show_hide(maclass,bool) {
	var laclass = document.getElementsByClassName(maclass);
	for (var i = 0; i < laclass.length ; i++) {
		if (bool)
			laclass[i].style.display = "table-cell";
		else
			laclass[i].style.display = "none";
	}
}

//--------------------------------------------------------------------------------------------------------//

function indice_change(inputs){
	var listid = [];
	for (var i = 0; i < inputs.length; i++) {
		if (inputs[i].toLowerCase() != '') {
			listid.push(i);
		}
	}
	return listid;
}

function show_hide_class(maclass) {
	var lediv = document.getElementsByClassName(maclass);
	for (var i = 0; i < lediv.length ; i++) {
		if (lediv[i].style.display == "none")
			lediv[i].style.display = "table-cell";
		else
			lediv[i].style.display = "none";
	}
}

function data_to_html(data){
	if( typeof(data) == "string"){
		return data;
	}
	text = "<table class=\"data\">";
	text+="<tr>";
	for(var h = 0; h < data[0].length;h++){
		text+="<td>"+data[0][h]+"</td>";
	}
	text+="</tr>";
	for (var i = 1; i < data.length-2; i++) {
		text+="<tr id="+i+">";
		for (var j = 0; j < data[i].length; j++) {
			text+="<td class="+j+">"+data[i][j]+"</td>";
		}
		text+="</tr>";
	}
	return text+"</table>";
}

function search_error(error_tab){
	var error = false;
	for (var i = 0; i < error_tab.length; i++) {
		var ligne = document.getElementById(i+1+"")
		for (var j = 0; j < error_tab[i].length; j++) {
			ligne.getElementsByClassName(error_tab[i][j]+"")[0].style.background ="#F5A9BC";
			error = true;
		}
	}
	return error;
}

function color_changed_data(changed_data){
	for (var i = 0; i < changed_data.length; i++) {
		var ligne = document.getElementById(i+1+"")
		for (var j = 0; j < changed_data[i].length; j++) {
			ligne.getElementsByClassName(changed_data[i][j]+"")[0].style.background ="#FE9A2E";
		}
	}
}

function affiche_tab(data,div){
	$("<table class=\"data\" >").appendTo(div);
	text = ""
	for (var i = 0; i < data.length; i++) {
		for (var j = 0; j < data[i].length; j++) {
			text+=data[i][j];
		}
	}
	$(text).appendTo(div+" table");
	show_hide("prelevement",show[0]);
	show_hide("preleveur",show[1]);
	show_hide("animal",show[2]);
	show_hide("cheptel",show[3]);
	show_hide("race",show[4]);
}

/* Recuperation des cookies */
/*
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
*/