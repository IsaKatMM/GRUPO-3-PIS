public class Actuador {
    //Atributo
    public double potencia;
    private String actuador;
    protected boolean estado;
    private String ubicacion;
    private String datosSensor;
    //Metodos
    public void cambiarEstado() {
         estado = !estado;
    }

    public boolean getEstado() {
        return estado;
    }

    public String getUbicacion() {
        return ubicacion;
    }
}
