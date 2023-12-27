function calcularPromedio() {
    var lecturaActual = parseFloat(document.getElementById("lecturaActual").value) || 0;
    var lecturaAnterior = parseFloat(document.getElementById("lecturaAnterior").value) || 0;

    var promedio = (lecturaActual + lecturaAnterior) / 2;

    alert("El promedio de las lecturas es: " + promedio);
  }