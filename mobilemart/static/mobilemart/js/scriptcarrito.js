document.addEventListener('DOMContentLoaded', function () {

    //API valor del dólar
    console.log("Esperando...");
    $.getJSON('https://mindicador.cl/api', function () {
    }).fail(function () {
        console.log('Error al consumir la API!');
        $("#dolar").text('Error al consumir la API!');
    }).done(function(data)
    {  
        $(".spinner").hide();
        $("#dolar").text("CLP$" + data.dolar.valor);
    });

});