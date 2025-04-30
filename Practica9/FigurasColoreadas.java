import java.util.Random;

// a) Interfaz Colorado
interface Colorado {
    String comoColorear();
}

// b) Clase abstracta Figura
abstract class Figura {
    private String color;
    
    public Figura(String color) {
        this.color = color;
    }
    
    public void setColor(String color) {
        this.color = color;
    }
    
    public String getColor() {
        return color;
    }
    
    @Override
    public String toString() {
        return "Figura de color " + color;
    }
    
    public abstract double area();
    public abstract double perimetro();
}

// c) Clase Cuadrado
class Cuadrado extends Figura implements Colorado {
    private double lado;
    
    public Cuadrado(String color, double lado) {
        super(color);
        this.lado = lado;
    }
    
    @Override
    public double area() {
        return lado * lado;
    }
    
    @Override
    public double perimetro() {
        return 4 * lado;
    }
    
    @Override
    public String comoColorear() {
        return "Colorear los cuatro lados";
    }
}

// d) Clase Circulo
class Circulo extends Figura {
    private double radio;
    
    public Circulo(String color, double radio) {
        super(color);
        this.radio = radio;
    }
    
    @Override
    public double area() {
        return Math.PI * radio * radio;
    }
    
    @Override
    public double perimetro() {
        return 2 * Math.PI * radio;
    }
}

// f) y g) Programa de prueba
public class FigurasColoreadas {
    public static void main(String[] args) {
        Figura[] figuras = new Figura[5];
        Random random = new Random();
        
        for (int i = 0; i < figuras.length; i++) {
            int tipo = random.nextInt(2) + 1;
            
            if (tipo == 1) { // Cuadrado
                double lado = 1 + random.nextDouble() * 9;
                figuras[i] = new Cuadrado("rojo", lado);
            } else { // Circulo
                double radio = 1 + random.nextDouble() * 9;
                figuras[i] = new Circulo("azul", radio);
            }
        }
        
        for (Figura figura : figuras) {
            System.out.println("Tipo: " + figura.getClass().getSimpleName());
            System.out.println("Color: " + figura.getColor());
            System.out.printf("Área: %.2f\n", figura.area());
            System.out.printf("Perímetro: %.2f\n", figura.perimetro());
            
            if (figura instanceof Colorado) {
                Colorado colorable = (Colorado) figura;
                System.out.println(colorable.comoColorear());
            }
            
            System.out.println("------------------------------");
        }
    }
}