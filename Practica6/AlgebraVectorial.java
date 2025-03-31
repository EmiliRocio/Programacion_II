public class AlgebraVectorial {
    private double x;
    private double y;
    private double z;
    
    public AlgebraVectorial() {
        this(0, 0, 0);
    }
    
    public AlgebraVectorial(double x, double y) {
        this(x, y, 0);
    }
    
    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    public double magnitud() {
        return Math.sqrt(x*x + y*y + z*z);
    }
    
    public double productoPunto(AlgebraVectorial otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }
    
    public AlgebraVectorial productoCruz(AlgebraVectorial otro) {
        double cruzX = this.y * otro.z - this.z * otro.y;
        double cruzY = this.z * otro.x - this.x * otro.z;
        double cruzZ = this.x * otro.y - this.y * otro.x;
        return new AlgebraVectorial(cruzX, cruzY, cruzZ);
    }
    
    // Inciso a) Perpendicular: |a + b| = |a - b|
    public boolean perpendicularA(AlgebraVectorial otro) {
        AlgebraVectorial suma = new AlgebraVectorial(
            this.x + otro.x, this.y + otro.y, this.z + otro.z);
        AlgebraVectorial resta = new AlgebraVectorial(
            this.x - otro.x, this.y - otro.y, this.z - otro.z);
        return Math.abs(suma.magnitud() - resta.magnitud()) < 1e-10;
    }
    
    // Inciso b) Perpendicular: |a - b| = |b - a|
    public boolean perpendicularB(AlgebraVectorial otro) {
        AlgebraVectorial resta1 = new AlgebraVectorial(
            this.x - otro.x, this.y - otro.y, this.z - otro.z);
        AlgebraVectorial resta2 = new AlgebraVectorial(
            otro.x - this.x, otro.y - this.y, otro.z - this.z);
        return Math.abs(resta1.magnitud() - resta2.magnitud()) < 1e-10;
    }
    
    // Inciso c) Perpendicular: a · b = 0
    public boolean perpendicularC(AlgebraVectorial otro) {
        return Math.abs(this.productoPunto(otro)) < 1e-10;
    }
    
    // Inciso d) Perpendicular: |a + b|² = |a|² + |b|²
    public boolean perpendicularD(AlgebraVectorial otro) {
        AlgebraVectorial suma = new AlgebraVectorial(
            this.x + otro.x, this.y + otro.y, this.z + otro.z);
        double sumaCuadrados = Math.pow(this.magnitud(), 2) + Math.pow(otro.magnitud(), 2);
        return Math.abs(Math.pow(suma.magnitud(), 2) - sumaCuadrados) < 1e-10;
    }
    
    // Inciso e) Paralela: a = r*b (existe un escalar r)
    public boolean paralelaE(AlgebraVectorial otro) {
        if (otro.x == 0 || otro.y == 0 || otro.z == 0) {
            // Manejar casos con componentes cero
            if (this.x == 0 && this.y == 0 && this.z == 0) return true;
            if (otro.x == 0 && this.x != 0) return false;
            if (otro.y == 0 && this.y != 0) return false;
            if (otro.z == 0 && this.z != 0) return false;
            
            // Encontrar componente no cero para calcular r
            double r = 0;
            if (otro.x != 0) r = this.x / otro.x;
            else if (otro.y != 0) r = this.y / otro.y;
            else if (otro.z != 0) r = this.z / otro.z;
            
            return Math.abs(this.x - otro.x * r) < 1e-10 &&
                   Math.abs(this.y - otro.y * r) < 1e-10 &&
                   Math.abs(this.z - otro.z * r) < 1e-10;
        }
        
        double r = this.x / otro.x;
        return Math.abs(this.y - otro.y * r) < 1e-10 &&
               Math.abs(this.z - otro.z * r) < 1e-10;
    }
    
    // Inciso f) Paralela: a × b = 0
    public boolean paralelaF(AlgebraVectorial otro) {
        return this.productoCruz(otro).magnitud() < 1e-10;
    }
    
    // Inciso g) Proyección de a sobre b: ((a·b)/(|b|²)) * b
    public AlgebraVectorial proyeccion(AlgebraVectorial otro) {
        double factor = this.productoPunto(otro) / Math.pow(otro.magnitud(), 2);
        return new AlgebraVectorial(
            otro.x * factor, 
            otro.y * factor, 
            otro.z * factor);
    }
    
    // Inciso h) Componente de a en b: (a·b)/|b|
    public double componente(AlgebraVectorial otro) {
        return this.productoPunto(otro) / otro.magnitud();
    }
    
    @Override
    public String toString() {
        return String.format("Vector(%.2f, %.2f, %.2f)", x, y, z);
    }
    
    public static void main(String[] args) {
        AlgebraVectorial v1 = new AlgebraVectorial(1, 0, 0);
        AlgebraVectorial v2 = new AlgebraVectorial(0, 1, 0);
        
        System.out.println("=== Pruebas de Perpendicularidad ===");
        System.out.println("Inciso a) |a+b|=|a-b|: " + v1.perpendicularA(v2));
        System.out.println("Inciso b) |a-b|=|b-a|: " + v1.perpendicularB(v2));
        System.out.println("Inciso c) a·b=0: " + v1.perpendicularC(v2));
        System.out.println("Inciso d) |a+b|²=|a|²+|b|²: " + v1.perpendicularD(v2));
        
        System.out.println("\n=== Pruebas de Paralelismo ===");
        AlgebraVectorial v3 = new AlgebraVectorial(2, 0, 0);
        System.out.println("Inciso e) a=rb: " + v1.paralelaE(v3));
        System.out.println("Inciso f) a×b=0: " + v1.paralelaF(v3));
        
        System.out.println("\n=== Proyección y Componente ===");
        AlgebraVectorial v4 = new AlgebraVectorial(1, 1, 0);
        AlgebraVectorial v5 = new AlgebraVectorial(2, 0, 0);
        System.out.println("Inciso g) Proyección de " + v4 + " sobre " + v5 + ": " + v4.proyeccion(v5));
        System.out.printf("Inciso h) Componente de %s en %s: %.2f\n", 
            v4, v5, v4.componente(v5));
    }
}