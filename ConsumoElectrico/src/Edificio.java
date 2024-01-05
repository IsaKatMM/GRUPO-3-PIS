public class Edificio {
    //Atributo
    private int numeroPisos;

    public static class Piso{
        public int numeroPiso; 
        private Edificio edificio;
     //constructor- da valores a atributos
        public Piso(Edificio edificio, int numeroPiso) {
            this.edificio = edificio;
            this.numeroPiso = numeroPiso;
        }
       //pisos se almacen en una lista
        private List<Piso> pisos = new ArrayList<>();
        
        public double CalcularConsumoPiso() {
            return 0;
        }

        public void crearPiso(int numeroPiso) {
            Piso nuevoPiso = new Piso(this, numeroPiso);
            pisos.add(nuevoPiso);
        }
        
    }

    //Metodo
    //suma el consumo de cada piso 
    public double calcularConsumoTotal() {
        double consumo = 0;
        for (Piso piso : pisos) {
            consumo += piso.CalcularConsumoPiso();
        }
        return consumo;
    }
}
