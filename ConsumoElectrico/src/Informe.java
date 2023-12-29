public class Informe {
    String contenido;
    String fecha;
    String hora;
    String ubicacion;
    String autor;
    String destinatario;
    String datosSensor;
    String datosActuador;
    String datosPiso;
    String datosEdificio;
    public void enviarInforme() {
    }

    public void archivarInforme() {
    }

    public void descargarInforme() {
    }
   public void generarInformePiso(String contenido, String fecha, String hora, String ubicacion, String autor, String
           destinatario, String datosSensor, String datosActuador, String datosPiso) {
        this.contenido = contenido;
        this.fecha = fecha;
        this.hora = hora;
        this.ubicacion = ubicacion;
        this.autor = autor;
        this.destinatario = destinatario;
        this.datosSensor = datosSensor;
        this.datosActuador = datosActuador;
        this.datosPiso = datosPiso;
    }
public void generarInformeEdificio(String contenido, String fecha, String hora, String ubicacion, String autor, String
        destinatario, String datosSensor, String datosActuador, String datosEdificio) {
        this.contenido = contenido;
        this.fecha = fecha;
        this.hora = hora;
        this.ubicacion = ubicacion;
        this.autor = autor;
        this.destinatario = destinatario;
        this.datosSensor = datosSensor;
        this.datosActuador = datosActuador;
        this.datosEdificio = datosEdificio;
    }
}