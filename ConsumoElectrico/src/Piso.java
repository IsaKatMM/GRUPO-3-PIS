public class Piso {
    //Atributos
    public Actuador[] actuadores;
    private String nombre;
    private String ubicacion;
    private String datosSensor;
    private String potenciaActuador;
    //Constructor
    // Inicializa los atributos de la clase cuando se crea una nueva instancia
    public void crearPiso(String nombre, String ubicacion, String datosSensor, String potenciaActuador) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
        this.datosSensor = datosSensor;
        this.potenciaActuador = potenciaActuador;
        this.actuadores = actuadores;
    }
    //Metodos
    public void obtenerRecomendaciones() {
        System.out.println("Obteniendo recomendaciones para el piso " + nombre);
    }

    // bucle que itera cada elemento
    public double calcularConsumoPiso() {
        double consumo = 0;
        for (Actuador actuador : actuadores) {
            consumo += actuador.potencia;
        }
        return consumo;
    }
    //Metodos get
     public Actuador[] getActuadores() {
        return actuadores;
    }

    public String getNombre() {
        return nombre;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public String getDatosSensor() {
        return datosSensor;
    }

}
