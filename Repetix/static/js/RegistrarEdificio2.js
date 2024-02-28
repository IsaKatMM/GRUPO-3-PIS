function registrarEdificio(){
    form.addEventListener('submit', function (event) {
        event.preventDefault() // Prevenir el comportamiento predeterminado del formulario
  
        const formData = new FormData(form)
        const consumoAnterior = formData.get('consumo_anterior')
        const consumoActual = formData.get('consumo_actual')
        const consumoSensor = formData.get('consumo_sensor')
  
        fetch('/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
          },
          body: JSON.stringify({
            consumo_anterior: consumoAnterior,
            consumo_actual: consumoActual,
            consumo_sensor: consumoSensor,
            codigo_edificio: '{{ edificio.codigo }}'
          })
        })
          .then((response) => response.json())
          .then((data) => {
            // Si el registro fue exitoso, mostrar el mensaje y deshabilitar el formulario
            if (data.success) {
              document.getElementById('mensajeRegistroPiso').style.display = 'block'
              form.reset()
              inputConsumoAnterior.disabled = true
              inputConsumoActual.disabled = true
              inputConsumoSensor.disabled = true
              submitButton.disabled = true
            } else {
              console.error('Error:', data.error)
            }
          })
          .catch((error) => console.error('Error:', error))
      })
}