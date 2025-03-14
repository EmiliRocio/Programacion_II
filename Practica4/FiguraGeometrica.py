import math

class FiguraGeometrica:
    def area(self, *args):
        if len(args) == 1:  # Círculo
            radio = args[0]
            return math.pi * radio ** 2
        elif len(args) == 2:  # Rectángulo o Triángulo rectángulo
            base, altura = args
            return base * altura
        elif len(args) == 3:  # Trapecio
            base_mayor, base_menor, altura = args
            return ((base_mayor + base_menor) / 2) * altura
        elif len(args) == 4:  # Pentágono (asumiendo un pentágono regular)
            lado, apotema = args[0], args[1]
            return (5 * lado * apotema) / 2
        else:
            raise ValueError("Número de argumentos no válido")

# Ejemplo de uso
figura = FiguraGeometrica()
print("Área del círculo:", figura.area(5))  # Círculo con radio 5
print("Área del rectángulo:", figura.area(4, 6))  # Rectángulo con base 4 y altura 6
print("Área del triángulo rectángulo:", figura.area(3, 4))  # Triángulo rectángulo con base 3 y altura 4
print("Área del trapecio:", figura.area(5, 3, 4))  # Trapecio con bases 5 y 3, y altura 4
print("Área del pentágono:", figura.area(5, 3))  # Pentágono regular con lado 5 y apotema 3