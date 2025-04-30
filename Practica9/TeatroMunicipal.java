import java.util.Scanner;

abstract class Boleto {
    protected int numero;
    
    public Boleto(int numero) {
        this.numero = numero;
    }
    
    public abstract double getPrecio();
    
    @Override
    public String toString() {
        return String.format("Numero: %d, Precio: %.1f", numero, getPrecio());
    }
}

class Palco extends Boleto {
    public Palco(int numero) {
        super(numero);
    }
    
    @Override
    public double getPrecio() {
        return 100.0;
    }
}

class Platea extends Boleto {
    private int diasAnticipacion;
    
    public Platea(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
    }
    
    @Override
    public double getPrecio() {
        if (diasAnticipacion >= 10) {
            return 50.0;
        } else {
            return 60.0;
        }
    }
}

class Galeria extends Boleto {
    private int diasAnticipacion;
    
    public Galeria(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
    }
    
    @Override
    public double getPrecio() {
        if (diasAnticipacion >= 10) {
            return 25.0;
        } else {
            return 30.0;
        }
    }
}

public class TeatroMunicipal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Sistema de Boletos del Teatro Municipal");
        System.out.println("1. Obtener información de boleto");
        System.out.println("2. Salir");
        
        while (true) {
            System.out.print("Seleccione una opción: ");
            String opcion = scanner.nextLine();
            
            if (opcion.equals("1")) {
                System.out.print("Tipo de boleto (palco/platea/galeria): ");
                String tipo = scanner.nextLine().toLowerCase();
                
                System.out.print("Número de boleto: ");
                int numero = Integer.parseInt(scanner.nextLine());
                
                Boleto boleto;
                
                if (tipo.equals("palco")) {
                    boleto = new Palco(numero);
                } else if (tipo.equals("platea")) {
                    System.out.print("Días de anticipación: ");
                    int dias = Integer.parseInt(scanner.nextLine());
                    boleto = new Platea(numero, dias);
                } else if (tipo.equals("galeria")) {
                    System.out.print("Días de anticipación: ");
                    int dias = Integer.parseInt(scanner.nextLine());
                    boleto = new Galeria(numero, dias);
                } else {
                    System.out.println("Tipo de boleto no válido");
                    continue;
                }
                
                System.out.println(boleto.toString());
                
            } else if (opcion.equals("2")) {
                System.out.println("Saliendo del programa...");
                break;
            } else {
                System.out.println("Opción no válida");
            }
        }
        
        scanner.close();
    }
}