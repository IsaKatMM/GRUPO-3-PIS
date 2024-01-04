public class Actuador {
    public double potencia;
    private String actuador;
    protected boolean estado;
    private String ubicacion;
    private String datosSensor;


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
