import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def producto_punto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_cruz(self, otro):
        x = self.y * otro.z - self.z * otro.y
        y = self.z * otro.x - self.x * otro.z
        z = self.x * otro.y - self.y * otro.x
        return AlgebraVectorial(x, y, z)
    
    # Inciso a) Perpendicular: |a + b| = |a - b|
    def perpendicular_metodo_a(self, otro):
        suma = AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
        resta = AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
        return math.isclose(suma.magnitud(), resta.magnitud())
    
    # Inciso b) Perpendicular: |a - b| = |b - a|
    def perpendicular_metodo_b(self, otro):
        resta1 = AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
        resta2 = AlgebraVectorial(otro.x - self.x, otro.y - self.y, otro.z - self.z)
        return math.isclose(resta1.magnitud(), resta2.magnitud())
    
    # Inciso c) Perpendicular: a · b = 0
    def perpendicular_metodo_c(self, otro):
        return math.isclose(self.producto_punto(otro), 0)
    
    # Inciso d) Perpendicular: |a + b|² = |a|² + |b|²
    def perpendicular_metodo_d(self, otro):
        suma = AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
        return math.isclose(suma.magnitud()**2, self.magnitud()**2 + otro.magnitud()**2)
    
    # Inciso e) Paralela: a = r*b (existe un escalar r)
    def paralela_metodo_e(self, otro):
        if otro.x == 0 or otro.y == 0 or otro.z == 0:
            # Manejar casos con componentes cero
            if self.x == 0 and self.y == 0 and self.z == 0:
                return True
            if otro.x == 0 and self.x != 0:
                return False
            if otro.y == 0 and self.y != 0:
                return False
            if otro.z == 0 and self.z != 0:
                return False
            
            # Encontrar componente no cero para calcular r
            r = 0
            if otro.x != 0:
                r = self.x / otro.x
            elif otro.y != 0:
                r = self.y / otro.y
            elif otro.z != 0:
                r = self.z / otro.z
            
            return (math.isclose(self.x, otro.x * r) and
                    math.isclose(self.y, otro.y * r) and
                    math.isclose(self.z, otro.z * r))
        
        r = self.x / otro.x
        return (math.isclose(self.y, otro.y * r) and 
               math.isclose(self.z, otro.z * r))
    
    # Inciso f) Paralela: a × b = 0
    def paralela_metodo_f(self, otro):
        cruz = self.producto_cruz(otro)
        return math.isclose(cruz.magnitud(), 0)
    
    # Inciso g) Proyección de a sobre b: ((a·b)/(|b|²)) * b
    def proyeccion(self, otro):
        factor = self.producto_punto(otro) / (otro.magnitud()**2)
        return AlgebraVectorial(otro.x * factor, otro.y * factor, otro.z * factor)
    
    # Inciso h) Componente de a en b: (a·b)/|b|
    def componente(self, otro):
        return self.producto_punto(otro) / otro.magnitud()
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Ejemplo de uso
if __name__ == "__main__":
    v1 = AlgebraVectorial(1, 0, 0)
    v2 = AlgebraVectorial(0, 1, 0)
    
    print("=== Pruebas de Perpendicularidad ===")
    print(f"Inciso a) |a+b|=|a-b|: {v1.perpendicular_metodo_a(v2)}")
    print(f"Inciso b) |a-b|=|b-a|: {v1.perpendicular_metodo_b(v2)}")
    print(f"Inciso c) a·b=0: {v1.perpendicular_metodo_c(v2)}")
    print(f"Inciso d) |a+b|²=|a|²+|b|²: {v1.perpendicular_metodo_d(v2)}")
    
    print("\n=== Pruebas de Paralelismo ===")
    v3 = AlgebraVectorial(2, 0, 0)
    print(f"Inciso e) a=rb: {v1.paralela_metodo_e(v3)}")
    print(f"Inciso f) a×b=0: {v1.paralela_metodo_f(v3)}")
    
    print("\n=== Proyección y Componente ===")
    v4 = AlgebraVectorial(1, 1, 0)
    v5 = AlgebraVectorial(2, 0, 0)
    print(f"Inciso g) Proyección de {v4} sobre {v5}: {v4.proyeccion(v5)}")
    print(f"Inciso h) Componente de {v4} en {v5}: {v4.componente(v5):.2f}")