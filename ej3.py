# Ejercicio 3 - Laboratorio: filtro combinado de componentes
# Se filtra recorriendo la lista original, sin crear una segunda lista de resultados.

class Componente:
    """Representa un componente del laboratorio."""

    def __init__(self, codigo, nombre, tipo, marca, stock, ubicacion):
        # Inicializa los atributos del componente.
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.stock = stock
        self.ubicacion = ubicacion

    def hay_stock(self):
        # Devuelve True si existe al menos una unidad.
        return self.stock > 0

    def mostrar_datos(self):
        # Presenta toda la información del componente.
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Stock: {self.stock}")
        print(f"Ubicación: {self.ubicacion}")


componentes = [
    Componente(1, "Teclado USB", "Periférico", "Logitech", 12, "Estante A"),
    Componente(2, "Mouse óptico", "Periférico", "Genius", 20, "Estante A"),
    Componente(3, "Memoria RAM 8 GB", "Memoria", "Kingston", 7, "Estante B"),
    Componente(4, "SSD 480 GB", "Almacenamiento", "Kingston", 5, "Estante C"),
    Componente(5, "Cable HDMI", "Cable", "Nisuta", 30, "Estante D"),
    Componente(6, "Fuente 600 W", "Energía", "Corsair", 4, "Estante E"),
    Componente(7, "Memoria RAM 16 GB", "Memoria", "Crucial", 9, "Estante B"),
    Componente(8, "Cable de red", "Cable", "TP-Link", 25, "Estante D"),
    Componente(9, "Disco rígido 1 TB", "Almacenamiento", "Seagate", 0, "Estante C"),
    Componente(10, "Webcam HD", "Periférico", "Logitech", 6, "Estante A"),
]


def filtrar_componentes(tipo_solicitado, stock_minimo):
    """Muestra componentes del tipo indicado con stock suficiente."""
    cantidad = 0
    mayor_stock = None

    print("\n--- Componentes que cumplen las condiciones ---")
    for componente in componentes:
        coincide_tipo = componente.tipo.casefold() == tipo_solicitado.strip().casefold()
        cumple_stock = componente.stock >= stock_minimo

        if coincide_tipo and cumple_stock:
            componente.mostrar_datos()
            print("-" * 30)
            cantidad += 1

            # Se compara manualmente el stock; no se utiliza max().
            if mayor_stock is None or componente.stock > mayor_stock.stock:
                mayor_stock = componente

    if cantidad == 0:
        print("No hay componentes que cumplan ambas condiciones.")
    else:
        print(f"Cantidad de componentes encontrados: {cantidad}")
        print("Componente con mayor stock:")
        mayor_stock.mostrar_datos()


if __name__ == "__main__":
    tipo = input("Ingrese el tipo de componente (por ejemplo, Periférico): ")
    try:
        minimo = int(input("Ingrese el stock mínimo: "))
        if minimo < 0:
            print("El stock mínimo no puede ser negativo.")
        else:
            filtrar_componentes(tipo, minimo)
    except ValueError:
        print("Error: debe ingresar un número entero para el stock mínimo.")