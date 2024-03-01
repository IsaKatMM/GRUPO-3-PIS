function calcularEnergiaEolica() {
    // Obtener los valores de los campos del formulario
    const velocidadViento = parseFloat(document.getElementById('velocidad_viento').value);
    const areaBarrido = parseFloat(document.getElementById('area_barrido').value);
    const densidadAire = parseFloat(document.getElementById('densidad_aire').value);
    const eficienciaSistema = parseFloat(document.getElementById('eficiencia_sistema').value);

    // Verificar si alguno de los valores es negativo
    if (velocidadViento < 0 || areaBarrido < 0 || densidadAire < 0 || eficienciaSistema < 0) {
        // Mostrar mensaje de alerta
        alert('Por favor, ingresa valores no negativos.');
        return; // Detener la ejecución de la función
    }

    // Calcular la energía eólica
    const energiaEolica = calcularEnergia(velocidadViento, areaBarrido, densidadAire, eficienciaSistema);

    // Mostrar el resultado en el elemento con id "resultado-generacion-eolica"
    const resultado = document.getElementById('resultado-generacion-eolica');
    resultado.innerHTML = `<p>Energía eólica generada: ${energiaEolica.toFixed(2)} vatios</p>`;

    // Crear gráfico
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Energía Eólica Generada"],
            datasets: [{
                label: 'Energía Eólica (vatios)',
                data: [energiaEolica],
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function calcularEnergia(velocidadViento, areaBarrido, densidadAire, eficienciaSistema) {
    // Realizar el cálculo de la energía eólica
    const energiaGenerada = 0.5 * densidadAire * areaBarrido * velocidadViento**3 * eficienciaSistema;
    return energiaGenerada;
}
