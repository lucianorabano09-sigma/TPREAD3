# Ejercicio 4 - Catálogo de videojuegos: consultas mediante métodos
# Todas las operaciones consultan los objetos sin modificarlos ni eliminarlos.

class Videojuego:
    """Representa un videojuego del catálogo."""

    def __init__(self, codigo, titulo, genero, plataforma, anio, horas_estimadas):
        # Inicializa los atributos del videojuego.
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio
        self.horas_estimadas = horas_estimadas

    def mostrar_datos(self):
        # Muestra todos los datos del videojuego.
        print(f"Código: {self.codigo}")
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Año: {self.anio}")
        print(f"Horas estimadas: {self.horas_estimadas}")

    def es_del_genero(self, genero):
        # Devuelve True si el género coincide, sin distinguir mayúsculas.
        return self.genero.casefold() == genero.strip().casefold()

    def supera_horas(self, cantidad):
        # Devuelve True si el juego supera la cantidad de horas indicada.
        return self.horas_estimadas > cantidad


videojuegos = [
    Videojuego(1, "Minecraft", "Sandbox", "PC", 2011, 80),
    Videojuego(2, "FIFA 24", "Deportes", "PlayStation", 2023, 35),
    Videojuego(3, "The Witcher 3", "RPG", "PC", 2015, 100),
    Videojuego(4, "Stardew Valley", "Simulación", "PC", 2016, 55),
    Videojuego(5, "God of War", "Acción", "PlayStation", 2018, 25),
    Videojuego(6, "Mario Kart 8", "Carreras", "Nintendo Switch", 2014, 20),
    Videojuego(7, "Hollow Knight", "Metroidvania", "PC", 2017, 40),
    Videojuego(8, "Portal 2", "Puzles", "PC", 2011, 10),
]


def buscar_por_codigo(codigo):
    """Devuelve el videojuego encontrado o None."""
    for juego in videojuegos:
        if juego.codigo == codigo:
            return juego
    return None


def consultar_genero(genero):
    """Muestra los videojuegos que coinciden con el género."""
    cantidad = 0
    for juego in videojuegos:
        if juego.es_del_genero(genero):
            juego.mostrar_datos()
            print("-" * 30)
            cantidad += 1
    if cantidad == 0:
        print("No hay videojuegos de ese género.")


def consultar_duracion(horas):
    """Muestra los videojuegos cuya duración supera las horas indicadas."""
    cantidad = 0
    for juego in videojuegos:
        if juego.supera_horas(horas):
            juego.mostrar_datos()
            print("-" * 30)
            cantidad += 1
    if cantidad == 0:
        print("No hay videojuegos que superen esa duración.")


if __name__ == "__main__":
    genero = input("Ingrese el género que desea consultar: ")
    print("\n--- Búsqueda por género ---")
    consultar_genero(genero)

    try:
        horas = float(input("\nIngrese una cantidad de horas: "))
        print("\n--- Videojuegos que superan esa duración ---")
        consultar_duracion(horas)

        codigo = int(input("\nIngrese el código del videojuego: "))
        print("\n--- Búsqueda por código ---")
        juego_encontrado = buscar_por_codigo(codigo)
        if juego_encontrado is not None:
            juego_encontrado.mostrar_datos()
        else:
            print("No se encontró un videojuego con ese código.")
    except ValueError:
        print("Error: ingrese un valor numérico válido.")