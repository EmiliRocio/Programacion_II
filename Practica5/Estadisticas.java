    import java.util.Scanner;

    public class Estadisticas {
    private double[] datos;

    public Estadisticas(double[] datos) {
        this.datos = datos;
    }

    public double promedio() {
        double suma = 0;
        for (double dato : datos) {
            suma += dato;
        }
        return suma / datos.length;
    }

    public double desviacion() {
        double prom = promedio();
        double suma = 0;
        for (double dato : datos) {
            suma += Math.pow(dato - prom, 2);
        }
        return Math.sqrt(suma / (datos.length - 1));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] datos = new double[10];
        System.out.print("Ingrese 10 números: ");
        for (int i = 0; i < 10; i++) {
            datos[i] = scanner.nextDouble();
        }

        Estadisticas estadisticas = new Estadisticas(datos);
        System.out.println("El promedio es " + estadisticas.promedio());
        System.out.println("La desviación estándar es " + estadisticas.desviacion());
    }

    
}