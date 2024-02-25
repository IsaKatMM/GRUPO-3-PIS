function mostrarRegistrarDepartamentos() {
    const numDepartamentos = document.getElementById('departamentos_piso').value;
    const container = document.getElementById('departamentos_container');
    container.innerHTML = '';

    for (let i = 1; i <= numDepartamentos; i++) {
        const label = document.createElement('label');
        label.textContent = `Registrar departamento ${i}: `;
        
        const link = document.createElement('a');
        link.href = "{% url 'registrar_departamentos' %}?num_departamentos=${numDepartamentos}";
        link.textContent = 'Registrar departamento';
        link.target = '_blank';

        container.appendChild(label);
        container.appendChild(link);
        container.appendChild(document.createElement('br'));
    }
}