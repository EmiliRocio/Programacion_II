class Ministerio:
    def __init__(self, nombre, direccion, nro_empleados=0, empleados=None, edades=None, sueldos=None):
        self.nombre = nombre
        self.direccion = direccion
        self.nro_empleados = nro_empleados
        self.empleados = empleados if empleados else []
        self.edades = edades if edades else []
        self.sueldos = sueldos if sueldos else []
    
    def __str__(self):
        return f"Ministerio de {self.nombre} - {self.direccion} ({self.nro_empleados} empleados)"
    
    # Sobrecarga del operador + para transferir empleados
    def __add__(self, otro):
        if otro.nro_empleados > 0:
            # Transferir el último empleado de otro a self
            empleado = otro.empleados.pop()
            edad = otro.edades.pop()
            sueldo = otro.sueldos.pop()
            
            self.empleados.append(empleado)
            self.edades.append(edad)
            self.sueldos.append(sueldo)
            
            otro.nro_empleados -= 1
            self.nro_empleados += 1
            
            print(f"Empleado {empleado} transferido de {otro.nombre} a {self.nombre}")
        else:
            print("No hay empleados para transferir")
        return self
    
    # Método para eliminar empleados por edad
    def eliminar_por_edad(self, edad_eliminar):
        indices_a_eliminar = []
        
        for i, edad in enumerate(self.edades):
            if edad == edad_eliminar:
                indices_a_eliminar.append(i)
        
        # Eliminar en orden inverso para no afectar los índices
        for i in sorted(indices_a_eliminar, reverse=True):
            del self.empleados[i]
            del self.edades[i]
            del self.sueldos[i]
            self.nro_empleados -= 1
        
        return len(indices_a_eliminar)
    
    # Método sobrecargado para mostrar empleados con menor edad o sueldo
    def mostrar_empleados(self, criterio='edad'):
        if not self.empleados:
            print("No hay empleados en este ministerio")
            return
        
        if criterio == 'edad':
            valor = min(self.edades)
            indices = [i for i, edad in enumerate(self.edades) if edad == valor]
            print(f"Empleados con menor edad ({valor} años):")
        elif criterio == 'sueldo':
            valor = min(self.sueldos)
            indices = [i for i, sueldo in enumerate(self.sueldos) if sueldo == valor]
            print(f"Empleados con menor sueldo (${valor}):")
        else:
            print("Criterio no válido")
            return
        
        for i in indices:
            nombre_completo = " ".join(self.empleados[i])
            print(f"- {nombre_completo}, Edad: {self.edades[i]}, Sueldo: ${self.sueldos[i]}")

# a) Instanciar 2 objetos Ministerio de diferente forma
# Primer ministerio (creado con datos directamente)
ministerio_salud = Ministerio(
    nombre="Salud",
    direccion="Av. Arce #1234, La Paz",
    nro_empleados=4,
    empleados=[
        ["Pedro", "Rojas", "Luna"],
        ["Lucy", "Sosa", "Rios"],
        ["Ana", "Perez", "Rojas"],
        ["Saul", "Arce", "Calle"]
    ],
    edades=[35, 43, 26, 29],
    sueldos=[2500, 3250, 2700, 2500]
)

# Segundo ministerio (creado vacío y luego agregando datos)
ministerio_educacion = Ministerio(
    nombre="Educación",
    direccion="Av. 6 de Agosto #2345, La Paz",
    nro_empleados=0
)

# Agregar empleados al segundo ministerio
ministerio_educacion.empleados = [
    ["Juan", "Gomez", "Perez"],
    ["Maria", "Lopez", "Gomez"],
    ["Carlos", "Fernandez", "Vargas"]
]
ministerio_educacion.edades = [40, 35, 28]
ministerio_educacion.sueldos = [3000, 2800, 2200]
ministerio_educacion.nro_empleados = 3

print("\n--- a) Objetos instanciados ---")
print(ministerio_salud)
print(ministerio_educacion)

# b) Eliminar a los empleados con edad X
edad_a_eliminar = 35
eliminados = ministerio_salud.eliminar_por_edad(edad_a_eliminar)

print(f"\n--- b) Se eliminaron {eliminados} empleados con edad {edad_a_eliminar} ---")
print("Empleados restantes en Ministerio de Salud:")
for emp in ministerio_salud.empleados:
    print("- " + " ".join(emp))

# c) Sobrecargar un operador para transferir empleados
print("\n--- c) Transferencia de empleado ---")
print("Antes de transferir:")
print(f"Ministerio Salud empleados: {ministerio_salud.nro_empleados}")
print(f"Ministerio Educación empleados: {ministerio_educacion.nro_empleados}")

# Transferir empleado usando sobrecarga de operador +
ministerio_salud + ministerio_educacion

print("\nDespués de transferir:")
print(f"Ministerio Salud empleados: {ministerio_salud.nro_empleados}")
print(f"Ministerio Educación empleados: {ministerio_educacion.nro_empleados}")

# d) Sobrecargar un Método para mostrar empleados
print("\n--- d1) Empleados con menor edad ---")
ministerio_salud.mostrar_empleados('edad')
ministerio_educacion.mostrar_empleados('edad')

print("\n--- d2) Empleados con menor sueldo ---")
ministerio_salud.mostrar_empleados('sueldo')
ministerio_educacion.mostrar_empleados('sueldo')