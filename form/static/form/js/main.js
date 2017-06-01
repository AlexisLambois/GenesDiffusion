function getData(indice,inputs,operateurs){
	$.ajax({
		type: "POST",
		url: "/ajax/printer/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs},
		success: function(data) {
			console.log(data)
			affiche_tab(data,"#data");
		}
	});
};

function getGenotypage(indice,inputs,operateurs){
	$.ajax({
		type: "GET",
		url: "/ajax/genoty/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs},
		success: function(data) {
			affiche_tab(data,"#data");
		}
	});
};

function insertAnimal(data){
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

function saveData(indice,inputs,operateurs){
	$.ajax({
		type: "POST",
		url: "/ajax/save/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs},
		success: function(data) {
			
		}
	});
};

function saveData_Genoty(indice,inputs,operateurs){
	$.ajax({
		type: "POST",
		url: "/ajax/save_geno/",
		data: {'indice': indice,'inputs':inputs,'operateurs':operateurs},
		success: function(data) {
			
		}
	});
};

function findData(table,input_id,insert){
	$.ajax({
		type: "POST",
		url: "/ajax/find/",
		data: {'table': table,'input_id':input_id},
		success: function(data) {
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

//function affiche_tab(data,div){
//	console.log(data);
//	$("<table class=\"data\" >").appendTo(div);
//	text = ""
//	for (var i = 0; i < data.length; i++) {
//		for (var j = 0; j < data[i].length; j++) {
//			text+=data[i][j];
//		}
//	}
//	$(text).appendTo(div+" table");
//}

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
