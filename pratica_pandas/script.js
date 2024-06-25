'use strict'

// utilizando JavaScript

async function fetchData() {
    try {
        var id_cidade = document.getElementById('input_cidade').value;
        id_cidade = parseInt(id_cidade)

        //const response = await fetch(`http://localhost:5000/cidade`)
        
        const response = await fetch(`http://127.0.0.1:5000/cidade/8`, {
            mode: 'no-cors',
            headers: {'Content-Type': 'application/json'},
            method: "GET"
        });
        /*
        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        */
        const data = await response.json();
        console.log(data);
    }
    catch (error) {
        console.log(error);
    }
}

/* Utilizando JQUERY

jQuery.support.cors = true;
$(document).ready(function(){
    var botao = $('#botao');
    var cidade = $('#resultado');
    
    botao.click(function(){
        var apiUrl = 'http://localhost:5000/cidade/1';
        
        $.ajax({
            url: apiUrl,
            type: 'GET',
            headers: {  'Access-Control-Allow-Origin': "*" },
            //crossDomain: true,
            //dataType: 'jsonp',
            success: function(dados) {
                cidade.html(`<p>${dados.name}</p>`);
            },
            error: function() {
                cidade.html(`<p>Não foi possível consultar a API!</p>`);
            }
        })
    })
});
*/