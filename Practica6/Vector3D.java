public class Vector3D {
    private final double x;
    private final double y;
    private final double z;

    public Vector3D() {
        this(0, 0, 0);
    }

    public Vector3D(double x, double y) {
        this(x, y, 0);
    }

    public Vector3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // Métodos de acceso
    public double getX() { return x; }
    public double getY() { return y; }
    public double getZ() { return z; }

    // Operaciones vectoriales
    public Vector3D mas(Vector3D otro) {  // inciso a
        return new Vector3D(x + otro.x, y + otro.y, z + otro.z);
    }

   

    public Vector3D multiplicar(double escalar) {  // inciso b
        return new Vector3D(x * escalar, y * escalar, z * escalar);
    }

    public Vector3D dividir(double escalar) {
        if (escalar == 0) throw new ArithmeticException("División por cero");
        return new Vector3D(x / escalar, y / escalar, z / escalar);
    }

    public double productoPunto(Vector3D otro) {  // inciso e
        return x * otro.x + y * otro.y + z * otro.z;
    }

    public Vector3D productoCruz(Vector3D otro) {  // inciso f
        return new Vector3D(
            y * otro.z - z * otro.y,
            z * otro.x - x * otro.z,
            x * otro.y - y * otro.x
        );
    }

    public double magnitud() {  // inciso c
        return Math.sqrt(productoPunto(this));
    }

    public Vector3D normalizar() {  // inciso d
        double mag = magnitud();
        if (mag == 0) throw new ArithmeticException("No se puede normalizar el vector cero");
        return dividir(mag);
    }

    public boolean esPerpendicular(Vector3D otro) {  // Figura 1
        return Math.abs(productoPunto(otro)) < 1e-10 || 
               Math.abs(mas(otro).magnitud() ) < 1e-10;
    }

    public Vector3D proyeccion(Vector3D otro) {  // Figura 2
        return otro.multiplicar(productoPunto(otro) / otro.productoPunto(otro));
    }

    public double componente(Vector3D otro) {  // Figura 2
        return productoPunto(otro) / otro.magnitud();
    }

    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }

    public static void main(String[] args) {
        // Creación de vectores
        Vector3D v1 = new Vector3D(1, 2, 3);
        Vector3D v2 = new Vector3D(4, 5, 6);

        // Operaciones básicas
        System.out.println("Suma (a): " + v1.mas(v2));
        
        System.out.println("Multiplicación por escalar (b): " + v1.multiplicar(2));
        System.out.println("División por escalar: " + v1.dividir(2));
        System.out.printf("Magnitud (c): %.2f\n", v1.magnitud());
        System.out.println("Normalizado (d): " + v1.normalizar());
        System.out.printf("Producto punto (e): %.2f\n", v1.productoPunto(v2));
        System.out.println("Producto cruz (f): " + v1.productoCruz(v2));

        // Operaciones avanzadas
        Vector3D v3 = new Vector3D(1, 0, 0);
        Vector3D v4 = new Vector3D(0, 1, 0);
        System.out.println("\nPerpendicularidad (Figura 1): " + v3.esPerpendicular(v4));
        System.out.println("Proyección (Figura 2): " + new Vector3D(2, 1, 0).proyeccion(v3));
        System.out.printf("Componente (Figura 2): %.2f\n", new Vector3D(2, 1, 0).componente(v3));
    }
}