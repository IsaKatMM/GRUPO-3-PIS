function mostrarRegistrarPisos() {
  const numPisos = document.getElementById('numero_pisos').value;
  const container = document.getElementById('pisos_container');
  container.innerHTML = '';

  for (let i = 1; i <= numPisos; i++) {
    const form = document.createElement('form');
    form.setAttribute('action', 'registrar_piso');
    form.setAttribute('method', 'POST');
    form.setAttribute('class', 'py-2');

    // Endpoint de la vista Django
    const url = '/ControlarEdificio/';

    form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario

      const formData = new FormData(form);

      fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF
        },
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            document.getElementById('mensajeRegistroPiso').style.display = 'block';
            form.reset();
            actualizarTablaPisos();
          } else {
            console.error('Error:', data.error);
          }
        })
        .catch(error => console.error('Error:', error));
    });

    const csrfToken = document.createElement('input')
    csrfToken.setAttribute('type', 'hidden')
    csrfToken.setAttribute('name', 'csrfmiddlewaretoken')
    csrfToken.setAttribute('value', getCookie('csrftoken')) // Obtener el token CSRF

    const label = document.createElement('label')
    label.textContent = `Datos del piso ${i}: `

    const inputConsumoAnterior = createInput('number', 'consumo_anterior', 'Consumo anterior del piso en kilowatts', true);
    const inputConsumoActual = createInput('number', 'consumo_actual', 'Consumo actual del piso en kilowatts', true);
    const inputConsumoSensor = createInput('number', 'consumo_sensor', 'Consumo del sensor del piso en kilowatts por hora', true);
    const inputPisoId = createInput('hidden', 'piso_id', '{{ piso.piso_id }}');
    const inputEdificioCodigo = createInput('hidden', 'codigo_edificio', '{{ edificio.codigo }}');

    const submitButton = document.createElement('button')
    submitButton.setAttribute('type', 'submit')
    submitButton.setAttribute('class', 'btn btn-info')
    submitButton.textContent = 'Registrar piso'

    form.appendChild(csrfToken)
    form.appendChild(inputPisoId) // Añadir el campo oculto para el ID del piso
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

// Función para crear un elemento de entrada
function createInput(type, name, placeholder, required = false) {
  const input = document.createElement('input');
  input.setAttribute('type', type);
  input.setAttribute('name', name);
  input.setAttribute('class', 'form-control');
  input.setAttribute('placeholder', placeholder);
  if (required) {
    input.setAttribute('required', 'true');
  }
  return input;
}

// Función para obtener el valor del token CSRF
function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}



function actualizarTabla() {
  fetch('/ControlarEdificio/')
    .then(response => response.json())
    .then(data => {
      const tbody = document.querySelector('tbody');
      tbody.innerHTML = ''; // Limpiar contenido actual de la tabla
      data.pisos.forEach(piso => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${piso.numero}</td>
          <td>${piso.consumo_anterior}</td>
          <td>${piso.consumo_actual}</td>
          <td>${piso.consumo_sensor}</td>
          <td>
            <a href="/control/${piso.codigo_edificio}" class="btn btn-info">Acceder al edificio</a>
          </td>
          <td>
            <a href="/EliminarEdificio/${piso.codigo_edificio}" class="btn btn-danger btnEliminacion">Eliminar Edificio</a>
          </td>
        `;
        tbody.appendChild(tr);
      });
    })
    .catch(error => console.error('Error:', error));
}