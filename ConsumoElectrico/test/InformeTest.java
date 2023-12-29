import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class InformeTest {
    @BeforeEach
    void setUp() {
        Informe informe = new Informe();
    }
    @Test
    void enviarInforme() {
        Informe informe = new Informe();
        informe.enviarInforme();
    }
    @Test
    void archivarInforme() {
        Informe informe = new Informe();
        informe.archivarInforme();
    }
    @Test
    void descargarInforme() {
        Informe informe = new Informe();
        informe.descargarInforme();
    }
    @Test
    void generarInformePiso() {
        Informe informe = new Informe();
        informe.generarInformePiso("contenido", "fecha", "hora", "ubicacion", "autor", "destinatario", "datosSensor", "datosActuador", "datosPiso");

        assertEquals("contenido", informe.contenido);
        assertEquals("fecha", informe.fecha);
        assertEquals("hora", informe.hora);
        assertEquals("ubicacion", informe.ubicacion);
        assertEquals("autor", informe.autor);
        assertEquals("destinatario", informe.destinatario);
        assertEquals("datosSensor", informe.datosSensor);
        assertEquals("datosActuador", informe.datosActuador);
        assertEquals("datosPiso", informe.datosPiso);
    }
    @Test
    void generarInformeEdificio() {
        Informe informe = new Informe();
        informe.generarInformeEdificio("contenido", "fecha", "hora", "ubicacion", "autor", "destinatario", "datosSensor", "datosActuador", "datosEdificio");

        assertEquals("contenido", informe.contenido);
        assertEquals("fecha", informe.fecha);
        assertEquals("hora", informe.hora);
        assertEquals("ubicacion", informe.ubicacion);
        assertEquals("autor", informe.autor);
        assertEquals("destinatario", informe.destinatario);
        assertEquals("datosSensor", informe.datosSensor);
        assertEquals("datosActuador", informe.datosActuador);
        assertEquals("datosEdificio", informe.datosEdificio);
    }
}
