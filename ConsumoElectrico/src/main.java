public class main {

        //Crea usuario y acciones relacionadas
        public static void main(String[] args) {
        Usuario usuario1 = new Usuario();
        usuario1.crearUsuario("Carlos", "Perez", "calosperez@gmail.com", "1020304");
        usuario1.modificarContrasena("010203");
        usuario1.iniciarSesion("carlosperez@gmail.com", "1020304");

                System.out.println("Usuario creado: \n" + usuario1.nombre  + "" + usuario1.apellido + "\n" +
                        usuario1.correo + "\n" + usuario1.contrasena);
                System.out.println("Usuario modificado: \n" + usuario1.nombre  + "" + usuario1.apellido + "\n" +
                        usuario1.correo + "\n" + usuario1.contrasena);
                System.out.println("Usuario iniciado: \n" + usuario1.nombre  + "" + usuario1.apellido + "\n" +
                        usuario1.correo + "\n" + usuario1.contrasena);

                //Crea edificio y acciones relacionadas
        Informe informe1 = new Informe();
        informe1.generarInformePiso("Informe", "Fecha: 19-11-2023", "Hora: 10:00 AM",
                "Ubicacion: Pitas", "Autor: Pablo Jaramillo", "Destinatario: Carlos Perez",
                "DatosSensor: 5 amperios, cada 5 horas", "DatosActuador: 24 Amperios al dia",
                "DatoPiso: Piso 1");
        informe1.generarInformeEdificio("Informe", "Fecha: 19-11-2023", "Hora: 10:00 AM",
                "Ubicacion: Pitas", "Autor: Pablo Jaramillo", "Destinatario: Carlos Perez",
                "DatosSensor: 5 amperios, cada 5 horas", "DatosActuador: 24 Amperios al dia",
                "DatoEdificio: Edificio 1");
        informe1.enviarInforme();
        informe1.archivarInforme();
        informe1.descargarInforme();

        //Imprime de resultados
                System.out.println("Informe generado Piso1: \n" + informe1.contenido + "\n" + informe1.fecha + "\n" +
                        informe1.hora + "\n" + informe1.ubicacion + "\n" + informe1.autor + "\n" + informe1.destinatario
                        + "\n" + informe1.datosSensor + "\n" + informe1.datosActuador + "\n" + informe1.datosPiso);
                System.out.println("Informe generado Edificio1: \n" + informe1.contenido + "\n" + informe1.fecha + "\n" +
                        informe1.hora + "\n" + informe1.ubicacion + "\n" + informe1.autor + "\n" + informe1.destinatario
                        + "\n" + informe1.datosSensor + "\n" + informe1.datosActuador + "\n" + informe1.datosEdificio);

    }
}
