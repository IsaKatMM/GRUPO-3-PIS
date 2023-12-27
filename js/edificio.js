function calcularConsumoTotal() {
    var calcularConsumoTotal1 = parseFloat(document.getElementById("calcularConsumoTotal1").value) || 0;
    var calcularConsumoTotal2 = parseFloat(document.getElementById("calcularConsumoTotal2").value) || 0;
    var calcularConsumoTotal3 = parseFloat(document.getElementById("calcularConsumoTotal3").value) || 0;

    var calcularConsumoTotal = calcularConsumoTotal1 + calcularConsumoTotal2 + calcularConsumoTotal3;
    alert("El consumo total es de " + calcularConsumoTotal + " amperios.");
  }