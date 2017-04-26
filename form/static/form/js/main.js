function getAnimal(indice,inputs){
	$.ajax({
		type: "GET",
		url: "/ajax/more/",
		data: {'indice': indice,'inputs':inputs,'ordre':document.getElementById('myonoffswitch').checked},
		success: function(data) {
			affiche_tab(data,"#tab1");
			return data
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

function saveData(indice,inputs){
	$.ajax({
		type: "POST",
		url: "/ajax/save/",
		data: {'indice': indice,'inputs':inputs},
		success: function(data) {
			
		}
	});
};

function genere_input(int,id){
	var text = "";
	for(var i=0; i<int; i++){
		text += ("<td class=\"" + id + "\"><input id=\""+i+"\" type=\"text\"/></td>");
	}
	return text;
}

function genere_champs(){
	
	var prelevement = ["Plaque","Position","Date Enregistrement","Date Demande","Date Extraction","Date Reception  Lille","Type de Materiel","Dosage","Conformite","Code Barre","Nombre Extraction","Echec Extraction","Statut VCG"];
	var preleveur = ["Numero Agrement","Nom"];
	var animal = ["Ordre","Date Insert/Up","Id","Nom","Sexe","Date de naissance","Pere","Mere","Pays","Jumeaux"];
	var race = ["Numero Race","Nom Race"];
	var cheptel = ["Cheptel Actuel","Detenteur Actuel"];

	var text = "";
//	for (var i = 0; i < prelevement.length; i++) {
//		text += "<td class=\"prelevement\">" + prelevement[i] + "</td>";
//	}
//	for (var i = 0; i < preleveur.length; i++) {
//		text += "<td class=\"preleveur\">" + preleveur[i] + "</td>";
//	}
	for (var i = 0; i < animal.length; i++) {
		text += "<td class=\"animal\">" + animal[i] + "</td>";
	}
	for (var i = 0; i < race.length; i++) {
		text += "<td class=\"race\">" + race[i] + "</td>";
	}
	for (var i = 0; i < cheptel.length; i++) {
		text += "<td class=\"cheptel\">" + cheptel[i] + "</td>";
	}
	return text;
}


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
	text = "<table class=\"data\">";
	text+="<tr>";
	for(var h = 0; h < data[0].length;h++){
		text+="<td>"+data[0][h]+"</td>";
	}
	text+="</tr>";
	for (var i = 1; i < data.length-1; i++) {
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

function affiche_tab(donne,div){
	$("<table class=\"data\" >").appendTo(div);
	$(donne).appendTo(div+" table");
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
