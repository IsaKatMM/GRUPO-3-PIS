function generarInforme() {
    var fechaActual = new Date();
    var hora = fechaActual.getHours();
    var minutos = fechaActual.getMinutes();

    var contenido = document.getElementById("contenido").value;
    var autor = document.getElementById("autor").value;
    var destinatario = document.getElementById("destinatario").value;
    var ubicacion = document.getElementById("ubicacion").value;
    var fecha = document.getElementById("fecha").value;
    var hora = document.getElementById("hora").value;
    var piso = document.getElementById("piso").value;
    var amperios = document.getElementById("amperios").value;
    var horas = document.getElementById("horas").value;

    var datosActuador = "Datos del Actuador: " + (amperios * horas) + " Amperios al día";

    var informeCompleto = "Contenido: " + contenido + "<br>"
        + "Autor: " + autor + "<br>"
        + "Destinatario: " + destinatario + "<br>"
        + "Ubicación: " + ubicacion + "<br>"
        + "Fecha: " + fecha + "<br>"
        + "Hora: " + hora + "<br>"
        + "Piso: " + piso + "<br>"
        + "Datos del Sensor: " + amperios + " Amperios cada " + horas + " horas" + "<br>"
        + datosActuador;

    var informeResult = document.getElementById("informe-result");
    informeResult.innerHTML = informeCompleto;

    document.getElementById("opciones-generar-informe").style.display = "block";
}

function enviarInforme() {
    alert("Enviando informe...");
}

function archivarInforme() {
    alert("Archivando informe...");
}

function descargarInforme() {
    alert("Descargando informe...");
}

function generarInformePiso() {
    alert("Generando informe del piso...");
}

function generarInformeEdificio() {
    alert("Generando informe del edificio...");
}