import java.util.ArrayList;

public class Sistema {

    ArrayList<Actuador> actuadorArrayList = new ArrayList<>(); //diagrama
    private Usuario usuario;
    private Informe informe;

    public void supervisarSistema() { //diagrama
    }

    public int getEstado() { //diagrama
        return 0;
    }

    public static class Edificio {
        private Sistema sistema;
    }

    public static class Sensor {
        private Sistema sistema;

        public void leerDatos() {
        }
    }

    public static class Actuador {
        private Sistema sistema;

        public void cambiarEstado() {
        }
    }

    ArrayList<Sensor> sensorList = new ArrayList<>(); // Inicialización de sensorList
    ArrayList<Actuador> actuadorList = new ArrayList<>(); // Inicialización de actuadorList

    public void suprevisarSistema() {
        for (Sensor sensor : sensorList) {
            sensor.leerDatos();
        }
    }

    public void controlarSistema() {
        for (Actuador actuador : actuadorList) {
            actuador.cambiarEstado();
        }
    }
}
