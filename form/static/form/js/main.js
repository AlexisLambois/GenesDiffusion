function getAnimal(indice,inputs){
	$.ajax({
		type: "GET",
		url: "/ajax/more/",
		data: {'indice': indice,'inputs':inputs},
		success: function(data) {
			affiche_tab(data,"#tab1");
		}
	});
};

function insertAnimal(data){
	$.ajax({
		type: "POST",
		url: "/ajax/add/",
		data: {'data':data},
		success: function(data) {
			document.getElementsByClassName('data')[0].innerHTML = "";
			document.getElementsByClassName('access')[0].innerHTML = "";		
			$("<h3>Les logs sont disponibles : " + data + "</h3>").appendTo(".access");
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

	var animal = ["Pays + Id","Nom","Sexe","Date de naissance","Pere","Mere","Pays","Jumeaux"];
	var race = ["Numero Race","Nom Race"];
	var cheptel = ["Cheptel Actuel","Detenteur Actuel"];

	var text = "";
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

function search_error(error_tab){
	var error = false;
	for (var i = 1; i < error_tab.length; i++) {
		var ligne = document.getElementById(i+"")
		for (var j = 0; j < error_tab[i].length; j++) {
			ligne.getElementsByClassName(error_tab[i][j]+"")[0].style.background ="#F5A9BC";
			error = true;
		}
	}
	return error;
}

function affiche_tab(donne,div){
	$("<table>").appendTo(div);
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
