function generarEnergiaEolica() {
    const velocidadViento = document.getElementById('velocidadViento').value;
    fetch('/generar_energia_eolica/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ velocidad_viento: velocidadViento })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultado').innerText = `Energía generada (eólica): ${data.energia_generada} kWh`;
        });
}
