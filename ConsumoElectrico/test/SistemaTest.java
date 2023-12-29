import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SistemaTest {
    private Sistema sistema;

    @BeforeEach
    void setUp() {
        sistema = new Sistema();
    }

    @Test
    void supervisarSistema() {
        sistema.supervisarSistema();
        assertEquals(0, sistema.getEstado());
    }

    @Test
    void controlarSistema() {
        sistema.controlarSistema();
        assertEquals(0, sistema.getEstado());
    }
}
