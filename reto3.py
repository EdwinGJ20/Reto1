


biblioteca = []


def agregar_libro(titulo, autor, genero, copias):
    libro = {"titulo": titulo, "autor": autor, "genero": genero, "copias": copias}
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")


def buscar_libro(criterio, valor):
    resultados = [libro for libro in biblioteca if libro[criterio].lower() == valor.lower()]
    if resultados:
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros con ese criterio.")


def prestar_libro(titulo):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower() and libro["copias"] > 0:
            libro["copias"] -= 1
            print(f"Has prestado el libro '{titulo}'.")
            return
    print("El libro no está disponible.")

#
def devolver_libro(titulo):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["copias"] += 1
            print(f"Has devuelto el libro '{titulo}'.")
            return
    print("El libro no pertenece a esta biblioteca.")


def mostrar_libros_disponibles():
    for libro in biblioteca:
        if libro["copias"] > 0:
            print(libro)


while True:
    print("\nSistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros disponibles")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        genero = input("Género del libro: ")
        copias = int(input("Número de copias disponibles: "))
        agregar_libro(titulo, autor, genero, copias)
    elif opcion == "2":
        criterio = input("¿Buscar por título, autor o género?: ").lower()

    elif opcion == "3":
        titulo = input("Título del libro a prestar: ")
        prestar_libro(titulo)

    elif opcion == "4":
        titulo = input("Título del libro a devolver: ")
        devolver_libro(titulo)
    elif opcion == "5":
        mostrar_libros_disponibles()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")