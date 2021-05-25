$(document).ready(function() {
    $("#Registrar").click(function(){
        var nombre = $('#nombre').val();
        var apellido = $('#apellido').val();
        var edad = $('#edad').val();
        console.log("nombre " + nombre)
        console.log("apellido " + apellido)
        console.log("edad " + edad)
        url_get = "http://localhost:5000/api/registro/" + nombre + "/" + apellido + "/" + edad
        console.log(url_get)
        $.ajax({
	        type: "GET",
            url: url_get
        }).then(function(data) {
            console.log(data)
            console.log("data: " + data)
            $('#resultado_text').text(data.mensaje);
        });
    });
});
