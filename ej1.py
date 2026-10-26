# Ejercicio 1 - Mesa de ayuda: consulta de tickets
# Este programa realiza únicamente consultas READ sobre objetos TicketSoporte.

class TicketSoporte:
    """Representa un ticket de soporte informático."""

    def __init__(self, numero, usuario, sector, problema, prioridad, estado):
        # Inicializa los atributos del ticket.
        self.numero = numero
        self.usuario = usuario
        self.sector = sector
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado

    def mostrar_datos(self):
        # Muestra ordenadamente todos los datos del ticket.
        print(f"Número: {self.numero}")
        print(f"Usuario: {self.usuario}")
        print(f"Sector: {self.sector}")
        print(f"Problema: {self.problema}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")


# Lista de objetos cargados en memoria.
tickets = [
    TicketSoporte(101, "Ana", "Administración", "No enciende la PC", "Alta", "Pendiente"),
    TicketSoporte(102, "Bruno", "Biblioteca", "Problema con la impresora", "Media", "Resuelto"),
    TicketSoporte(103, "Carla", "Laboratorio", "Sin conexión a Internet", "Alta", "Pendiente"),
    TicketSoporte(104, "Diego", "Dirección", "Error al iniciar sesión", "Baja", "En proceso"),
    TicketSoporte(105, "Elena", "Administración", "Teclado dañado", "Media", "Pendiente"),
    TicketSoporte(106, "Facundo", "Biblioteca", "No abre un archivo", "Baja", "Resuelto"),
    TicketSoporte(107, "Gabriela", "Laboratorio", "Monitor sin imagen", "Alta", "Pendiente"),
    TicketSoporte(108, "Hugo", "Dirección", "Sistema lento", "Media", "En proceso"),
]


def buscar_ticket(numero):
    """Devuelve el ticket encontrado o None si no existe."""
    for ticket in tickets:
        if ticket.numero == numero:
            return ticket
    return None


def mostrar_pendientes():
    """Muestra los tickets pendientes y cuenta cuántos hay."""
    cantidad = 0
    print("\n--- Tickets pendientes ---")
    for ticket in tickets:
        if ticket.estado.lower() == "pendiente":
            ticket.mostrar_datos()
            print("-" * 30)
            cantidad += 1
    print(f"Cantidad de tickets pendientes: {cantidad}")


if __name__ == "__main__":
    try:
        numero = int(input("Ingrese el número de ticket que desea consultar: "))
        encontrado = buscar_ticket(numero)

        # El mensaje de error se muestra una sola vez, luego de finalizar la búsqueda.
        if encontrado is not None:
            encontrado.mostrar_datos()
        else:
            print("Ticket no encontrado")

        mostrar_pendientes()
    except ValueError:
        print("Error: debe ingresar un número entero.")