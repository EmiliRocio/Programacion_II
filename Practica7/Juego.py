import random

class Juego:
    def __init__(self, vidas_iniciales):
        self.numeroDeVidas = vidas_iniciales
        self.record = 0
    
    def reiniciaPartida(self):
        pass
    
    def actualizaRecord(self):
        pass
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas_iniciales):
        super().__init__(vidas_iniciales)
        self.numeroAAdivinar = 0
    
    def reiniciaPartida(self):
        self.numeroAAdivinar = random.randint(0, 10)
    
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    
    def juega(self):
        self.reiniciaPartida()
        print(f"\n--- Nuevo juego: Adivina un número entre 0 y 10 ---")
        
        while True:
            print(f"\nVidas restantes: {self.numeroDeVidas}")
            print(f"Record actual: {self.record}")
            
            try:
                numero = int(input("Introduce tu número: "))
            except ValueError:
                print("Error: Debes ingresar un número entero.")
                continue
            
            if not self.validaNumero(numero):
                print("Error: El número debe estar entre 0 y 10.")
                continue
            
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"¡Game Over! El número era {self.numeroAAdivinar}")
                    break
                print("Número incorrecto. ¡Sigue intentando!")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            return False
        if numero % 2 != 0:
            print("Error: Debes ingresar un número PAR.")
            return False
        return True

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            return False
        if numero % 2 == 0:
            print("Error: Debes ingresar un número IMPAR.")
            return False
        return True

class Aplicacion:
    @staticmethod
    def main():
        juegos = [
            JuegoAdivinaNumero(3),
            JuegoAdivinaPar(3),
            JuegoAdivinaImpar(3)
        ]
        
        for juego in juegos:
            juego.juega()
            input("\nPresiona Enter para continuar al siguiente juego...")

if __name__ == "__main__":
    Aplicacion.main()