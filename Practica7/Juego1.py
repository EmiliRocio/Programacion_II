import random

class Juego1:
    def __init__(self):
        self.numeroDeVidas = 0
        self.record = 0
    
    def reiniciaPartida(self):
        # Este método debería ser implementado en la clase hija
        pass
    
    def actualizaRecord(self):
        # Este método debería ser implementado en la clase hija
        pass
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego1):
    def __init__(self, numeroDeVidas):
        super().__init__()
        self.numeroDeVidas = numeroDeVidas
        self.numeroAAdivinar = 0
    
    def reiniciaPartida(self):
        self.numeroAAdivinar = random.randint(0, 10)
    
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    
    def juega(self):
        self.reiniciaPartida()
        
        while True:
            print("\n--- Nuevo intento ---")
            print(f"Vidas restantes: {self.numeroDeVidas}")
            print("Record actual: {self.record}")
            
            try:
                numero = int(input("Adivina un número entre 0 y 10: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
            
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"¡Game Over! El número era {self.numeroAAdivinar}")
                    break
                else:
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es mayor.")
                    else:
                        print("El número a adivinar es menor.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)  # 3 vidas iniciales
        print("¡Bienvenido al juego de adivinar el número!")
        print("Tienes que adivinar un número entre 0 y 10.")
        juego.juega()
        
        while True:
            continuar = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if continuar == 's':
                juego = JuegoAdivinaNumero(3)
                juego.juega()
            elif continuar == 'n':
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Por favor, ingresa 's' o 'n'.")

if __name__ == "__main__":
    Aplicacion.main()