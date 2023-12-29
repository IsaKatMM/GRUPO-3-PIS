import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ActuadorTest {
    @BeforeEach
    void setUp() {
        Actuador actuador = new Actuador();
        }
    @Test
    void cambiarEstado() {
        Actuador actuador = new Actuador();
        actuador.cambiarEstado();

        assertEquals(true, actuador.getEstado());
    }
}