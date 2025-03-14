public class FiguraGeometric {
	

    // Área del círculo
    double area(double radio) {
        return Math.PI * radio * radio;
    }

    // Área del rectángulo
    double areaRectangulo(double base, double altura) {
        return base * altura;
    }

    // Área del triángulo rectángulo
    double areaTrianguloRectangulo(double base, double altura) {
        return (base * altura) / 2;
    }

    // Área del trapecio
    double area(double baseMayor, double baseMenor, double altura) {
        return ((baseMayor + baseMenor) / 2) * altura;
    }

    // Área del pentágono regular
    double area(double lado, double apotema) {
        return (5 * lado * apotema) / 2;
    }

    public static void main(String[] args) {
        FiguraGeometric figura = new FiguraGeometric();

        System.out.println("Área del círculo: " + figura.area(5));
        System.out.println("Área del rectángulo: " + figura.areaRectangulo(4, 6)); 
        System.out.println("Área del triángulo rectángulo: " + figura.areaTrianguloRectangulo(3, 4)); 
        System.out.println("Área del trapecio: " + figura.area(5, 3, 4)); 
        System.out.println("Área del pentágono: " + figura.area(5, 3)); 
    }


}
