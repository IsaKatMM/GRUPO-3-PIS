function calcularEnergiaEolica() {
    // Obtener los valores de los campos del formulario
    const velocidadViento = parseFloat(document.getElementById('velocidad_viento').value);
    const areaBarrido = parseFloat(document.getElementById('area_barrido').value);
    const densidadAire = parseFloat(document.getElementById('densidad_aire').value);
    const eficienciaSistema = parseFloat(document.getElementById('eficiencia_sistema').value);

    // Calcular la energía eólica
    const energiaEolica = calcularEnergia(velocidadViento, areaBarrido, densidadAire, eficienciaSistema);

    // Mostrar el resultado en el elemento con id "resultado-generacion-eolica"
    const resultado = document.getElementById('resultado-generacion-eolica');
    resultado.innerHTML = `<p>Energía eólica generada: ${energiaEolica.toFixed(2)} vatios</p>`;
}

function calcularEnergia(velocidadViento, areaBarrido, densidadAire, eficienciaSistema) {
    // Aquí se realiza el cálculo de la energía eólica
    // Puedes usar las fórmulas que consideres adecuadas para tu aplicación
    const energiaGenerada = 0.5 * densidadAire * areaBarrido * velocidadViento**3 * eficienciaSistema;
    return energiaGenerada;
}
