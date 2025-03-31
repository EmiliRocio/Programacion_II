import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # Sobrecarga de operadores aritméticos
    def __add__(self, otro):  # a + b (inciso a)
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):  # a - b
        return Vector3D(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __mul__(self, escalar):  # a * k (inciso b)
        if isinstance(escalar, (int, float)):
            return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)
        raise TypeError("Solo se puede multiplicar por escalares")

    def __rmul__(self, escalar):  # k * a
        return self.__mul__(escalar)

    def __truediv__(self, escalar):  # a / k
        if escalar == 0:
            raise ZeroDivisionError("División por cero")
        return Vector3D(self.x / escalar, self.y / escalar, self.z / escalar)

    # Operaciones vectoriales
    def __matmul__(self, otro):  # a @ b (producto punto) (inciso e)
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def __mod__(self, otro):  # a % b (producto cruz) (inciso f)
        return Vector3D(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )

    # Métodos de instancia
    def magnitud(self):  # inciso c
        return math.sqrt(self @ self)

    def normalizar(self):  # inciso d
        mag = self.magnitud()
        if mag == 0:
            raise ValueError("No se puede normalizar el vector cero")
        return self / mag

    def es_perpendicular(self, otro):  # Figura 1
        return math.isclose(self @ otro, 0) or math.isclose((self + otro).magnitud(), (self - otro).magnitud())

    def proyeccion(self, otro):  # Figura 2
        return ((self @ otro) / (otro @ otro)) * otro

    def componente(self, otro):  # Figura 2
        return (self @ otro) / otro.magnitud()

    # Representaciones
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Ejemplo de uso
if __name__ == "__main__":
    # Creación de vectores
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)

    # Operaciones básicas
    print(f"Suma (a): {v1 + v2}")
    print(f"Resta: {v1 - v2}")
    print(f"Multiplicación por escalar (b): {2 * v1}")
    print(f"División por escalar: {v1 / 2}")
    print(f"Magnitud (c): {v1.magnitud():.2f}")
    print(f"Normalizado (d): {v1.normalizar()}")
    print(f"Producto punto (e): {v1 @ v2}")
    print(f"Producto cruz (f): {v1 % v2}")

    # Operaciones avanzadas
    v3 = Vector3D(1, 0, 0)
    v4 = Vector3D(0, 1, 0)
    print(f"\nPerpendicularidad (Figura 1): {v3.es_perpendicular(v4)}")
    print(f"Proyección (Figura 2): {Vector3D(2, 1, 0).proyeccion(v3)}")
    print(f"Componente (Figura 2): {Vector3D(2, 1, 0).componente(v3):.2f}")