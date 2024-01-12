public class Informe {
    //Atributos
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
    //Metodos
    public void enviarInforme() {
        System.out.println("Enviando informe...");
    }

    public void archivarInforme() {
        System.out.println("Archivando informe...");
    }

    public void descargarInforme() {
        System.out.println("Descargando informe...");
    }
    //Constructor
    //Asignar valores a los atributos de la instancia actual
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

    // toma varios parámetros para inicializar los atributos de un objeto
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
