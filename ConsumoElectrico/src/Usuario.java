public class Usuario {
    String nombre;
    String apellido;
    String correo;
    String contrasena;

    public void crearUsuario(String nombre, String apellido, String correo, String contrasena) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.correo = correo;
        this.contrasena = contrasena;
    }

    public boolean iniciarSesion(String correo, String contrasena) {
        if (this.correo == correo && this.contrasena == contrasena) {
            return true;
        } else {
            return false;
        }
    }
    public boolean cerrarSesion() {
        return true;
    }

    public void modificarContrasena(String contrasena) {
        this.contrasena = contrasena;
    }

    public boolean eliminarUsuario() {

        return true;
    }

    public boolean verificarUsuario() {
        return true;
    }
}
