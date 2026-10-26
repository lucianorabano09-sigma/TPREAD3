# Ejercicio 5 - Servicio técnico: menú de consultas de reparaciones
# El menú realiza exclusivamente operaciones READ: no modifica ni elimina objetos.

class Reparacion:
    """Representa una reparación registrada en el servicio técnico."""

    def __init__(self, orden, cliente, equipo, falla, estado, tecnico, costo_estimado):
        # Inicializa los atributos de la reparación.
        self.orden = orden
        self.cliente = cliente
        self.equipo = equipo
        self.falla = falla
        self.estado = estado
        self.tecnico = tecnico
        self.costo_estimado = costo_estimado

    def mostrar_datos(self):
        # Muestra todos los datos de la reparación.
        print(f"Orden: {self.orden}")
        print(f"Cliente: {self.cliente}")
        print(f"Equipo: {self.equipo}")
        print(f"Falla: {self.falla}")
        print(f"Estado: {self.estado}")
        print(f"Técnico: {self.tecnico}")
        print(f"Costo estimado: ${self.costo_estimado:.2f}")


reparaciones = [
    Reparacion(1001, "Lucía Pérez", "Notebook", "No carga la batería", "Pendiente", "Martín", 45000),
    Reparacion(1002, "Juan Gómez", "PC de escritorio", "No enciende", "En proceso", "Sofía", 38000),
    Reparacion(1003, "Marta Díaz", "Impresora", "Atasco de papel", "Finalizada", "Martín", 12000),
    Reparacion(1004, "Pedro Ruiz", "Notebook", "Pantalla dañada", "Pendiente", "Carlos", 95000),
    Reparacion(1005, "Ana Torres", "Tablet", "No responde el táctil", "En proceso", "Sofía", 52000),
    Reparacion(1006, "Diego López", "PC de escritorio", "Falla de disco", "Finalizada", "Carlos", 61000),
    Reparacion(1007, "Elena Castro", "Monitor", "Sin imagen", "Pendiente", "Martín", 30000),
    Reparacion(1008, "Nicolás Silva", "Notebook", "Sistema lento", "Finalizada", "Sofía", 18000),
    Reparacion(1009, "Paula Fernández", "Impresora", "No imprime", "En proceso", "Carlos", 24000),
    Reparacion(1010, "Tomás Herrera", "Tablet", "Problema de carga", "Pendiente", "Sofía", 27000),
]


def buscar_por_orden(numero):
    """Devuelve la reparación con esa orden o None si no existe."""
    for reparacion in reparaciones:
        if reparacion.orden == numero:
            return reparacion
    return None


def filtrar_por_estado(estado):
    """Muestra las reparaciones cuyo estado coincide."""
    cantidad = 0
    for reparacion in reparaciones:
        if reparacion.estado.casefold() == estado.strip().casefold():
            reparacion.mostrar_datos()
            print("-" * 30)
            cantidad += 1
    if cantidad == 0:
        print("No se encontraron reparaciones con ese estado.")


def filtrar_por_tecnico(tecnico):
    """Muestra las reparaciones asignadas al técnico indicado."""
    cantidad = 0
    for reparacion in reparaciones:
        if reparacion.tecnico.casefold() == tecnico.strip().casefold():
            reparacion.mostrar_datos()
            print("-" * 30)
            cantidad += 1
    if cantidad == 0:
        print("No se encontraron reparaciones asignadas a ese técnico.")


def filtrar_por_costo(limite):
    """Muestra reparaciones cuyo costo es menor o igual al límite."""
    cantidad = 0
    for reparacion in reparaciones:
        if reparacion.costo_estimado <= limite:
            reparacion.mostrar_datos()
            print("-" * 30)
            cantidad += 1
    if cantidad == 0:
        print("No hay reparaciones dentro de ese límite de costo.")


def mostrar_todas():
    """Muestra todos los registros cargados."""
    for reparacion in reparaciones:
        reparacion.mostrar_datos()
        print("-" * 30)


def menu():
    """Mantiene el programa activo hasta seleccionar la opción Salir."""
    while True:
        print("\n===== SERVICIO TÉCNICO =====")
        print("1) Mostrar todas")
        print("2) Buscar por orden")
        print("3) Filtrar por estado")
        print("4) Filtrar por técnico")
        print("5) Filtrar por costo")
        print("6) Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_todas()
        elif opcion == "2":
            try:
                numero = int(input("Ingrese el número de orden: "))
                reparacion = buscar_por_orden(numero)
                if reparacion is None:
                    print("No se encontró esa orden.")
                else:
                    reparacion.mostrar_datos()
            except ValueError:
                print("Error: la orden debe ser un número entero.")
        elif opcion == "3":
            estado = input("Ingrese el estado (Pendiente, En proceso o Finalizada): ")
            filtrar_por_estado(estado)
        elif opcion == "4":
            tecnico = input("Ingrese el nombre del técnico: ")
            filtrar_por_tecnico(tecnico)
        elif opcion == "5":
            try:
                limite = float(input("Ingrese el costo máximo: "))
                if limite < 0:
                    print("El costo no puede ser negativo.")
                else:
                    filtrar_por_costo(limite)
            except ValueError:
                print("Error: ingrese un importe numérico válido.")
        elif opcion == "6":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida. Seleccione un número del 1 al 6.")


if __name__ == "__main__":
    menu()