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
    
    public void actualizaRecord() {
        if (numeroDeVidas > record) {
            record = numeroDeVidas;
        }
    }
    
    public boolean quitaVida() {
        numeroDeVidas--;
        return numeroDeVidas > 0;
    }
}

class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;
    protected Random random;
    
    public JuegoAdivinaNumero(int vidasIniciales) {
        super(vidasIniciales);
        this.random = new Random();
    }
    
    @Override
    public void reiniciaPartida() {
        numeroAAdivinar = random.nextInt(11);
    }
    
    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }
    
    public void juega(Scanner scanner) {
        reiniciaPartida();
        System.out.println("\n--- Nuevo juego: Adivina un número entre 0 y 10 ---");
        
        while (true) {
            System.out.println("\nVidas restantes: " + numeroDeVidas);
            System.out.println("Record actual: " + record);
            
            System.out.print("Introduce tu número: ");
            int numero;
            try {
                numero = scanner.nextInt();
            } catch (Exception e) {
                System.out.println("Error: Debes ingresar un número entero.");
                scanner.next();
                continue;
            }
            
            if (!validaNumero(numero)) {
                System.out.println("Error: El número debe estar entre 0 y 10.");
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
                }
                System.out.println("Número incorrecto. ¡Sigue intentando!");
            }
        }
    }
}

class JuegoAdivinaPar extends JuegoAdivinaNumero {
    public JuegoAdivinaPar(int vidasIniciales) {
        super(vidasIniciales);
    }
    
    @Override
    public boolean validaNumero(int numero) {
        if (!super.validaNumero(numero)) {
            return false;
        }
        if (numero % 2 != 0) {
            System.out.println("Error: Debes ingresar un número PAR.");
            return false;
        }
        return true;
    }
}

class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    public JuegoAdivinaImpar(int vidasIniciales) {
        super(vidasIniciales);
    }
    
    @Override
    public boolean validaNumero(int numero) {
        if (!super.validaNumero(numero)) {
            return false;
        }
        if (numero % 2 == 0) {
            System.out.println("Error: Debes ingresar un número IMPAR.");
            return false;
        }
        return true;
    }
}

public class Aplicacion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        JuegoAdivinaNumero juegoNormal = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(3);
        
        System.out.println("=== JUEGO DE ADIVINAR NÚMERO NORMAL ===");
        juegoNormal.juega(scanner);
        
        System.out.println("\n=== JUEGO DE ADIVINAR NÚMERO PAR ===");
        juegoPar.juega(scanner);
        
        System.out.println("\n=== JUEGO DE ADIVINAR NÚMERO IMPAR ===");
        juegoImpar.juega(scanner);
        
        System.out.println("\n¡Gracias por jugar!");
        scanner.close();
    }
}