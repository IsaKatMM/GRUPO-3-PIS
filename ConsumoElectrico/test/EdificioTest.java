import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EdificioTest {
    Edificio edificio;

    @BeforeEach
    void setUp() {
        edificio = new Edificio();
    }
    @Test
    void Piso() {
        Edificio.Piso piso = new Edificio.Piso();

    //assertEquals = Afirmación

        assertEquals(0, piso.CalcularConsumoPiso());
    }
    @Test
    void calcularConsumoTotal() {
        assertEquals(0, edificio.calcularConsumoTotal());
    }
}
