public class Usuario {
    //Atributos
    String nombre;
    String apellido;
    String correo;
    String contrasena;
    //Metodos
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
         System.out.println("Sesión cerrada.");
        return true;
    }

    public void modificarContrasena(String nuevaContrasena) {
        this.contrasena = nuevaContrasena;
        System.out.println("Contraseña modificada.");
    }

    public boolean eliminarUsuario() {
        System.out.println("Usuario eliminado.");
        return true;
    }

    public boolean verificarUsuario() {
        System.out.println("Usuario verificado.");
        return true;
    }

        // Métodos getter para obtener información del usuario
    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getCorreo() {
        return correo;
    }

}
