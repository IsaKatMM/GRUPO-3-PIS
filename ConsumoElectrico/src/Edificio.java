public class Edificio {
    //Atributo
    private int numeroPisos;

    public static class Piso{
        public int numeroPiso; 
        private Edificio edificio;

        public Piso(Edificio edificio, int numeroPiso) {
            this.edificio = edificio;
            this.numeroPiso = numeroPiso;
        }

        private List<Piso> pisos = new ArrayList<>();
        
        public double CalcularConsumoPiso() {
            return 0;
        }

        public void crearPiso(int numeroPiso) {
            Piso nuevoPiso = new Piso(this, numeroPiso);
            pisos.add(nuevoPiso);
        }
        
    }
    public double calcularConsumoTotal() {
        double consumo = 0;
        for (Piso piso : pisos) {
            consumo += piso.CalcularConsumoPiso();
        }
        return consumo;
    }
}
