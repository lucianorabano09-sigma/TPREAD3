# Ejercicio 2 - Biblioteca multimedia: búsqueda flexible
# Este programa busca títulos sin distinguir mayúsculas de minúsculas.

class RecursoDigital:
    """Representa un recurso digital de una biblioteca escolar."""

    def __init__(self, codigo, titulo, categoria, autor, anio, disponible):
        # Inicializa los atributos del recurso.
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    def mostrar_resumen(self):
        # Muestra los datos solicitados en la consigna.
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Código: {self.codigo} | Título: {self.titulo}")
        print(f"Categoría: {self.categoria} | Disponibilidad: {estado}")


# Lista con diez recursos de diferentes categorías.
recursos = [
    RecursoDigital(1, "Introducción a Python", "Libro digital", "Laura Pérez", 2022, True),
    RecursoDigital(2, "Python desde cero", "Tutorial", "Marcos Díaz", 2023, True),
    RecursoDigital(3, "Historia de la programación", "Video educativo", "Sofía Ruiz", 2021, False),
    RecursoDigital(4, "Manual de redes", "Manual", "Pablo Gómez", 2020, True),
    RecursoDigital(5, "Revista de tecnología", "Revista", "Equipo editorial", 2024, False),
    RecursoDigital(6, "Programación orientada a objetos", "Libro digital", "Ana López", 2022, True),
    RecursoDigital(7, "Seguridad informática básica", "Tutorial", "Nicolás Torres", 2023, True),
    RecursoDigital(8, "Algoritmos explicados", "Video educativo", "Julia Fernández", 2021, False),
    RecursoDigital(9, "Guía de HTML y CSS", "Manual", "Pedro Sánchez", 2024, True),
    RecursoDigital(10, "Python para principiantes", "Revista", "Camila Castro", 2025, False),
]


def buscar_por_titulo(texto):
    """Muestra todos los títulos que contienen el texto ingresado."""
    coincidencias = 0
    disponibles = 0
    texto = texto.strip().casefold()

    for recurso in recursos:
        # casefold permite comparar texto sin distinguir mayúsculas/minúsculas.
        if texto in recurso.titulo.casefold():
            recurso.mostrar_resumen()
            print(f"Autor: {recurso.autor} | Año: {recurso.anio}")
            print("-" * 40)
            coincidencias += 1
            if recurso.disponible:
                disponibles += 1

    if coincidencias == 0:
        print("No se encontraron recursos que coincidan con la búsqueda.")
    else:
        print(f"Cantidad total de coincidencias: {coincidencias}")
        print(f"Cantidad de recursos disponibles: {disponibles}")


if __name__ == "__main__":
    palabra = input("Ingrese una palabra o parte del título: ")
    buscar_por_titulo(palabra)