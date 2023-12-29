import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SensorTest {
    @BeforeEach
    void setUp() {
        Sensor sensor = new Sensor();
    }
@Test
    void leerDatos() {
        Sensor sensor = new Sensor();
        sensor.leerDatos();

        assertEquals(0, sensor.getDatos());
    }


}