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

function file_verif(filepath){
	console.log(filepath);
	return filepath;
}

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

function affiche_tab(donne,div){
	$("<table>").appendTo(div);
	$(donne).appendTo(div+" table");
}