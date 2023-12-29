import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UsuarioTest {
    Usuario usuario;

    @BeforeEach
    void setUp() {
        usuario = new Usuario();
    }

    @Test
    void crearUsuario() {
        usuario.crearUsuario("Juan", "Perez", "correo@gmail.com", "12345");

        //assertEquals = Afirmación

        assertEquals("Juan", usuario.nombre);
        assertEquals("Perez", usuario.apellido);
        assertEquals("correo@gmail.com", usuario.correo);
        assertEquals("12345", usuario.contrasena);
    }
    @Test
    void iniciarSesion() {
        usuario.crearUsuario("Juan", "Perez", "correo@gmail.com", "12345");
        assertEquals(true, usuario.iniciarSesion("correo@gmail.com", "12345"));
    }
    @Test
    void cerrarSesion() {
        assertEquals(true, usuario.cerrarSesion());
    }
    @Test
void modificarContrasena() {
        usuario.crearUsuario("Juan", "Perez", "correo@gmail.com", "12345");
    }
    @Test
    void eliminarUsuario() {
        assertEquals(true, usuario.eliminarUsuario());
    }
    @Test
    void verificarUsuario() {
        assertEquals(true, usuario.verificarUsuario());
    }

}
