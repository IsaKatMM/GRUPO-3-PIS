function mostrarRegistrarPisos() {
    const numPisos = document.getElementById('numero_pisos').value;
    const container = document.getElementById('pisos_container');
    container.innerHTML = '';

    for (let i = 1; i <= numPisos; i++) {
        const label = document.createElement('label');
        label.textContent = `Registrar piso ${i}: `;
        
        const link = document.createElement('a');
//        link.href = `registrar_pisos_${i}.html`;                
//              link.href = `/registrar_pisos.html?num_pisos=${numPisos}/`;
        link.href = "{% url 'registrar_pisos' %}?num_pisos=${numPisos}";
//              link.href = "{% url 'registrar_pisos' %}?numero_edificio={{ edificio.id }}";
        link.textContent = 'Registrar piso';
        link.target = '_blank';

        container.appendChild(label);
        container.appendChild(link);
        container.appendChild(document.createElement('br'));
    }
}