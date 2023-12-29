import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PisoTest {
    Edificio.Piso piso;

    @BeforeEach
    void setUp() {
        piso = new Edificio.Piso();
    }
    @Test
    void calcularconsumoPiso() {
        Edificio.Piso piso = new Edificio.Piso();

    //assertEquals = Afirmación

        assertEquals(0, piso.CalcularConsumoPiso());
    }
    @Test
    void crearPiso() {
        Edificio.Piso piso = new Edificio.Piso();
        piso.crearPiso(1);

        assertEquals(1, piso.numeroPiso);
    }
}
