public class Piso {
    public Actuador[] actuadores;
    private String nombre;

    private String ubicacion;
    private String datosSensor;
    private String potenciaActuador;


    public void crearPiso(String nombre, String ubicacion, String datosSensor, String potenciaActuador) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
        this.datosSensor = datosSensor;
        this.potenciaActuador = potenciaActuador;
    }

    public void obtenerRecomendaciones() {
    }

    public double CalcularConsumoPiso() {
        double consumo = 0;
        for (Actuador actuador : actuadores) {
            consumo += actuador.potencia;
        }
        return consumo;
    }
}
