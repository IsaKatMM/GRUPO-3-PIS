public class Actuador {
    //Atributo
    public double potencia;
    private String actuador;
    protected boolean estado;
    private String ubicacion;
    private String datosSensor;
    //Metodos
    //hace cambiar el valor del estado al contrario del valor actual
    public void cambiarEstado() {
         estado = !estado;
    }
    //acceder al atributo privado- get
    public boolean getEstado() {
        return estado;
    }

    public String getUbicacion() {
        return ubicacion;
    }
}
