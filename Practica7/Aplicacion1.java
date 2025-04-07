import java.util.Scanner;
import java.util.Random;

class Juego {
    protected int numeroDeVidas;
    protected int record;
    
    public Juego(int vidasIniciales) {
        this.numeroDeVidas = vidasIniciales;
        this.record = 0;
    }
    
    public void reiniciaPartida() {}
    
    public void actualizaRecord() {}
    
    public boolean quitaVida() {
        numeroDeVidas--;
        return numeroDeVidas > 0;
    }
}

class JuegoAdivinaNumero extends Juego {
    private int numeroAAdivinar;
    private Random random;
    
    public JuegoAdivinaNumero(int vidasIniciales) {
        super(vidasIniciales);
        this.random = new Random();
    }
    
    @Override
    public void reiniciaPartida() {
        numeroAAdivinar = random.nextInt(11); // Números 0-10
    }
    
    @Override
    public void actualizaRecord() {
        if (numeroDeVidas > record) {
            record = numeroDeVidas;
        }
    }
    
    public void juega(Scanner scanner) {
        reiniciaPartida();
        
        while (true) {
            System.out.println("\n--- Nuevo intento ---");
            System.out.println("Vidas restantes: " + numeroDeVidas);
            System.out.println("Record actual: " + record);
            
            System.out.print("Adivina un número entre 0 y 10: ");
            int numero;
            try {
                numero = scanner.nextInt();
            } catch (Exception e) {
                System.out.println("Error: Debes ingresar un número entero.");
                scanner.next(); // Limpiar buffer
                continue;
            }
            
            if (numero == numeroAAdivinar) {
                System.out.println("¡Acertaste!");
                actualizaRecord();
                break;
            } else {
                if (!quitaVida()) {
                    System.out.println("¡Game Over! El número era " + numeroAAdivinar);
                    break;
                } else {
                    System.out.println(numero < numeroAAdivinar ? 
                        "El número es mayor." : "El número es menor.");
                }
            }
        }
    }
}

public class Aplicacion1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        JuegoAdivinaNumero juego = new JuegoAdivinaNumero(3);
        
        System.out.println("¡Bienvenido al juego de adivinar el número!");
        
        do {
            juego.juega(scanner);
            System.out.print("\n¿Jugar otra vez? (s/n): ");
        } while (scanner.next().equalsIgnoreCase("s"));
        
        System.out.println("¡Gracias por jugar!");
        scanner.close();
    }
}