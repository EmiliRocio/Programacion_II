class LineaTeleferico:
    def __init__(self, color, tramo, nro_cabinas, nro_empleados, empleados=None, edades=None, sueldos=None):
        self.color = color
        self.tramo = tramo
        self.nro_cabinas = nro_cabinas
        self.nro_empleados = nro_empleados
        self.empleados = empleados if empleados else []
        self.edades = edades if edades else []
        self.sueldos = sueldos if sueldos else []
    
    def __str__(self):
        return f"Línea {self.color}: {self.tramo} ({self.nro_cabinas} cabinas, {self.nro_empleados} empleados)"
    
    # Sobrecarga del operador + para transferir empleados
    def __add__(self, otro):
        if self.nro_empleados > 0:
            # Transferir el último empleado de self a otro
            empleado = self.empleados.pop()
            edad = self.edades.pop()
            sueldo = self.sueldos.pop()
            
            otro.empleados.append(empleado)
            otro.edades.append(edad)
            otro.sueldos.append(sueldo)
            
            self.nro_empleados -= 1
            otro.nro_empleados += 1
            
            print(f"Empleado {empleado} transferido de línea {self.color} a línea {otro.color}")
        else:
            print("No hay empleados para transferir")
        return self
    
    # Método para eliminar empleados por apellido
    def eliminar_por_apellido(self, apellido):
        indices_a_eliminar = []
        
        for i, empleado in enumerate(self.empleados):
            if apellido in empleado:
                indices_a_eliminar.append(i)
        
        # Eliminar en orden inverso para no afectar los índices
        for i in sorted(indices_a_eliminar, reverse=True):
            del self.empleados[i]
            del self.edades[i]
            del self.sueldos[i]
            self.nro_empleados -= 1
        
        return len(indices_a_eliminar)
    
    # Método sobrecargado para mostrar empleados con mayor edad o sueldo
    def mostrar_empleados(self, criterio='edad'):
        if not self.empleados:
            print("No hay empleados en esta línea")
            return
        
        if criterio == 'edad':
            max_valor = max(self.edades)
            indices = [i for i, edad in enumerate(self.edades) if edad == max_valor]
            print(f"Empleados con mayor edad ({max_valor} años):")
        elif criterio == 'sueldo':
            max_valor = max(self.sueldos)
            indices = [i for i, sueldo in enumerate(self.sueldos) if sueldo == max_valor]
            print(f"Empleados con mayor sueldo (${max_valor}):")
        else:
            print("Criterio no válido")
            return
        
        for i in indices:
            print(f"- {self.empleados[i]}, Edad: {self.edades[i]}, Sueldo: ${self.sueldos[i]}")

# a) Instanciar 2 objetos LineaTeleferico de diferente forma
# Primera línea (creada con datos directamente)
linea_roja = LineaTeleferico(
    color="Rojo",
    tramo="Estación Central, Estación Cementerio, Estación 16 de Julio",
    nro_cabinas=20,
    nro_empleados=4,
    empleados=[["Pedro", "Rojas", "Luna"], ["Lucy", "Sosa", "Rios"], 
               ["Ana", "Perez", "Rojas"], ["Saul", "Arce", "Calle"]],
    edades=[35, 50, 26, 29],
    sueldos=[2500, 3250, 2700, 2500]
)





print("\n--- a) Objetos instanciados ---")
print(linea_roja)


# b) Eliminar a los empleados con apellido X, paterno o materno
apellido_a_eliminar = "Rojas"
eliminados = linea_roja.eliminar_por_apellido(apellido_a_eliminar)

print(f"\n--- b) Se eliminaron {eliminados} empleados con apellido '{apellido_a_eliminar}' ---")
print("Empleados restantes en línea roja:")
for emp in linea_roja.empleados:
    print("- " + " ".join(emp))

# c) Sobrecargar un operador para transferir empleados
print("\n--- c) Transferencia de empleado ---")
print("Antes de transferir:")
print(f"Línea Roja empleados: {linea_roja.nro_empleados}")
# Transferir empleado usando sobrecarga de operador +
linea_roja 

print("\nDespués de transferir:")
print(f"Línea Roja empleados: {linea_roja.nro_empleados}")


# d) Sobrecargar un Método para mostrar empleados
print("\n--- d1) Empleados con mayor edad ---")
linea_roja.mostrar_empleados('edad')


print("\n--- d2) Empleados con mayor sueldo ---")
linea_roja.mostrar_empleados('sueldo')