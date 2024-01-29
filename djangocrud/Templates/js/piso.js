function calcularConsumoTotal() {
  var amperios = parseFloat(document.getElementById("amperios").value) || 0;
  var horas = parseFloat(document.getElementById("horas").value) || 0;

  var consumoTotal = amperios * horas;

  alert("El consumo total es de " + consumoTotal + " amperios.");

  if (consumoTotal > 700) {
    alert("¡Consumo Alto detectado! Reduzca el Consumo.");
  }
}
