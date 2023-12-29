public class Edificio {
    private int numeroPisos;

    public static class Piso{
        public int numeroPiso; //diagrama
        private Edificio edificio;

        public double CalcularConsumoPiso() {
            return 0;
        }

        public void crearPiso(int i) { //diagrama
            this.numeroPiso = i;
        }
    }
    public double calcularConsumoTotal() {
        double consumo = 0;
        Piso[] pisos = new Piso[0];
        for (Piso piso : pisos) {
            consumo += piso.CalcularConsumoPiso();
        }
        return consumo;
    }
}
