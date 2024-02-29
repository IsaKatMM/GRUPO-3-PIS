function mostrarRegistrarPisos() {
  const numPisos = document.getElementById('numero_pisos').value;
  const container = document.getElementById('pisos_container');
  container.innerHTML = '';

  for (let i = 1; i <= numPisos; i++) {
    const form = document.createElement('form');
    form.setAttribute('method', 'POST');
    form.setAttribute('class', 'py-2');

    // Aquí debes agregar el endpoint de tu vista Django
    const url = '/registrar_piso/';

    form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario

      const formData = new FormData(form);

      fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': '{{ csrf_token }}'
        },
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            document.getElementById('mensajeRegistroPiso').style.display = 'block';
            form.reset();
          } else {
            console.error('Error:', data.error);
          }
        })
        .catch(error => console.error('Error:', error));
    });

    const csrfToken = document.createElement('input')
    csrfToken.setAttribute('type', 'hidden')
    csrfToken.setAttribute('name', 'csrfmiddlewaretoken')
    csrfToken.setAttribute('value', '{{ csrf_token }}')

    const label = document.createElement('label')
    label.textContent = `Datos del piso ${i}: `

    const inputConsumoAnterior = document.createElement('input')
    inputConsumoAnterior.setAttribute('type', 'number')
    inputConsumoAnterior.setAttribute('name', 'consumo_anterior')
    inputConsumoAnterior.setAttribute('class', 'form-control')
    inputConsumoAnterior.setAttribute('placeholder', 'Consumo anterior del piso en kilowatts')
    inputConsumoAnterior.setAttribute('required', 'true')

    const inputConsumoActual = document.createElement('input')
    inputConsumoActual.setAttribute('type', 'number')
    inputConsumoActual.setAttribute('name', 'consumo_actual')
    inputConsumoActual.setAttribute('class', 'form-control')
    inputConsumoActual.setAttribute('placeholder', 'Consumo actual del piso en kilowatts')
    inputConsumoActual.setAttribute('required', 'true')

    const inputConsumoSensor = document.createElement('input')
    inputConsumoSensor.setAttribute('type', 'number')
    inputConsumoSensor.setAttribute('name', 'consumo_sensor')
    inputConsumoSensor.setAttribute('class', 'form-control')
    inputConsumoSensor.setAttribute('placeholder', 'Consumo del sensor del piso en kilowatts por hora')
    inputConsumoSensor.setAttribute('required', 'true')

    // Hidden input for unique ID of the floor
    const inputPisoId = document.createElement('input')
    inputPisoId.setAttribute('type', 'hidden')
    inputPisoId.setAttribute('name', 'piso_id')
    inputPisoId.setAttribute('value', '{{ uuid.uuid4 }}')

    const inputEdificioCodigo = document.createElement('input')
    inputEdificioCodigo.setAttribute('type', 'hidden')
    inputEdificioCodigo.setAttribute('name', 'codigo_edificio')
    inputEdificioCodigo.setAttribute('value', '{{ edificio.codigo }}')

    const submitButton = document.createElement('button')
    submitButton.setAttribute('type', 'submit')
    submitButton.setAttribute('class', 'btn btn-info')
    submitButton.textContent = 'Registrar piso'

    form.addEventListener('submit', function (event) {
      event.preventDefault() // Prevenir el comportamiento predeterminado del formulario

      const formData = new FormData(form)
      const consumoAnterior = formData.get('consumo_anterior')
      const consumoActual = formData.get('consumo_actual')
      const consumoSensor = formData.get('consumo_sensor')

      fetch('/registrar_piso/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({
          consumo_anterior: consumoAnterior,
          consumo_actual: consumoActual,
          consumo_sensor: consumoSensor,
          codigo_edificio: '{{ edificio.codigo }}',
          piso_id: '{{ uuid.uuid4 }}'
        })
      })
        .then((response) => response.json())
        .then((data) => {
          // Si el registro fue exitoso, mostrar el mensaje y deshabilitar los campos
          if (data.success) {
            document.getElementById('mensajeRegistroPiso').style.display = 'block';
            inputConsumoAnterior.disabled = true;
            inputConsumoActual.disabled = true;
            inputConsumoSensor.disabled = true;
            submitButton.disabled = true;
          } else {
            console.error('Error:', data.error)
          }
        })
        .catch((error) => console.error('Error:', error))
    })

    form.appendChild(csrfToken)
    form.appendChild(inputPisoId) // Append hidden input for piso ID
    form.appendChild(label)
    form.appendChild(document.createElement('br'))
    form.appendChild(inputConsumoAnterior)
    form.appendChild(document.createElement('br'))
    form.appendChild(inputConsumoActual)
    form.appendChild(document.createElement('br'))
    form.appendChild(inputConsumoSensor)
    form.appendChild(document.createElement('br'))
    form.appendChild(inputEdificioCodigo)
    form.appendChild(document.createElement('br'))
    form.appendChild(submitButton)

    container.appendChild(form)
    container.appendChild(document.createElement('br'))
  }
}