public class Sensor {
    //Atributos
    private String numero;
    protected boolean estado;
    private String ubicacion;
    protected double lecturaActual;
    protected double lecturaAnterior;
    //Metodos
    public void leerDatos() {
        System.out.println("Leyendo datos del sensor " + numero);
    }

    public int getDatos() {
        return lecturaActual;
    }
    //Constructor
    public Sensor(String numero, boolean estado, String ubicacion) {
        this.numero = numero;
        this.estado = estado;
        this.ubicacion = ubicacion;
    }
    //Metodos get
    public String getNumero() {
        return numero;
    }

    public boolean getEstado() {
        return estado;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public double getLecturaActual() {
        return lecturaActual;
    }

    public double getLecturaAnterior() {
        return lecturaAnterior;
    }

}
