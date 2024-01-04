import java.util.ArrayList;

public class Sistema {

    ArrayList<Actuador> actuadorArrayList = new ArrayList<>();
    ArrayList<Sensor> sensorList = new ArrayList<>();
    private ArrayList<Actuador> actuadorList = new ArrayList<>();
    private Usuario usuario;
    private Informe informe;

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

    public static class Edificio {
        private Sistema sistema;
        public Edificio(Sistema sistema) {
            this.sistema = sistema;
        }
    }

    public static class Sensor {
        private Sistema sistema;
        public Sensor(Sistema sistema) {
            this.sistema = sistema;
        }
        public void leerDatos() {
            System.out.println("Leyendo datos del sensor en el sistema.");
        }
    }

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
