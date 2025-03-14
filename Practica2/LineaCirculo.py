import math
import matplotlib.pyplot as plt
import pandas as pd

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y  

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x * self.x + self.y * self.y)
        angulo = math.atan2(self.y, self.x)
        angulo = math.degrees(angulo)
        return radio, angulo

    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y)

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Línea desde {self.p1} hasta {self.p2}"

    def dibujaLinea(self):
        return f"Dibujando línea desde {self.p1} hasta {self.p2}"
    def graficar(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], marker='o', label=str(self))

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio de {self.radio:.2f}"

    def dibujaCirculo(self):
        return f"Dibujando círculo con centro en {self.centro} y radio de {self.radio:.2f}"
    def graficar(self):
        circle = plt.Circle((self.centro.x, self.centro.y), self.radio, color='blue', fill=False, label=str(self))
        plt.gca().add_patch(circle)

# Ejemplo de uso:
p1 = Punto(0, 3)
p2 = Punto(3, 4)
linea = Linea(p1, p2)
circulo = Circulo(p1, 5)

print(linea)
print(linea.dibujaLinea())
print(circulo)
print(circulo.dibujaCirculo())
linea.graficar()
circulo.graficar()

# Configuraciones adicionales del gráfico
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.title('Gráfico de Línea y Círculo')
plt.show()