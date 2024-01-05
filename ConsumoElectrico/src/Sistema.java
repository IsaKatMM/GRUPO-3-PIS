import java.util.ArrayList;

public class Sistema {

    //Atributos
    ArrayList<Actuador> actuadorArrayList = new ArrayList<>(); //Se inicializa vacio
    ArrayList<Sensor> sensorList = new ArrayList<>(); //Se inicializa vacio
    ArrayList<Actuador> actuadorList = new ArrayList<>(); //Se inicializa vacio
    //relacion de asociacion
    private Usuario usuario;
    private Informe informe;

    //Metodos
    public void supervisarSistema() {
        for (Sensor sensor : sensorList) {
            sensor.leerDatos();
        }
    }

    public void controlarSistema() {
        for (Actuador actuador : actuadorList) {
            actuador.cambiarEstado();
        }
    }

    //CLases internas
    //relacion de composiciom
    public static class Edificio {
        private Sistema sistema;
        public Edificio(Sistema sistema) {
            this.sistema = sistema;
        }
    }
    //relacion de composiciom
    public static class Sensor {
        private Sistema sistema;
        public Sensor(Sistema sistema) {
            this.sistema = sistema;
        }
        public void leerDatos() {
            System.out.println("Leyendo datos del sensor en el sistema.");
        }
    }
    //relacion de composiciom
    public static class Actuador {
        private Sistema sistema;
        public Actuador(Sistema sistema) {
            this.sistema = sistema;
        }
        public void cambiarEstado() {
           System.out.println("Cambiando estado del actuador en el sistema."); 
        }
    }
}
