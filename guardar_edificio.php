<?php
// Verificar si se recibieron los datos del formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recuperar los datos del formulario
    $nombreEdificio = $_POST['nombre_edificio'];
    $numeroEdificio = $_POST['numero_edificio'];
    $ubicacionEdificio = $_POST['ubicacion_edificio'];
    $numeroPisos = $_POST['numero_pisos'];

    // Aquí puedes realizar las operaciones necesarias con los datos, como almacenarlos en una base de datos, enviar por correo electrónico, etc.
    
    // Por ejemplo, simplemente imprimir los datos para demostración
    echo "Nombre del edificio: " . $nombreEdificio . "<br>";
    echo "Número del edificio: " . $numeroEdificio . "<br>";
    echo "Ubicación del edificio: " . $ubicacionEdificio . "<br>";
    echo "Número de pisos del edificio: " . $numeroPisos . "<br>";

    // Redireccionar de vuelta al formulario después de procesar los datos
    header("Location: RegistrarEdificio.html");
    exit(); // Asegurarse de que el script se detenga aquí
}
?>
