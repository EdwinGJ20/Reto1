def menu():
    print("\nInventario Básico")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")


def AgregaProducto(inventario):
    nombre = input("Nombre del producto: ").strip()
    cantidad = int(input("Cantidad: "))

    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            print(f"Se agregó {cantidad} unidades al stock de {nombre}.")
            return

    inventario.append([nombre, cantidad])
    print(f"Producto {nombre} agregado con {cantidad} unidades.")


def MostrarInventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\nInventario:")
    for producto in inventario:
        print(f"{producto[0]} - {producto[1]} unidades")


def VenderProducto(inventario):
    nombre = input("Nombre del producto a vender: ").strip()

    for producto in inventario:
        if producto[0] == nombre:
            cantidad = int(input(f"Cantidad a vender de {nombre} (disponible: {producto[1]}): "))
            if cantidad > producto[1]:
                print("No hay suficiente stock.")
            else:
                producto[1] -= cantidad
                print(f"Se vendió {cantidad} unidades de {nombre}.")
                if producto[1] == 0:
                    inventario.remove(producto)
                    print(f"{nombre} se ha agotado y fue eliminado del inventario.")
            return

    print("Producto no encontrado en el inventario.")


def main():
    inventario = []

    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            AgregaProducto(inventario)
        elif opcion == "2":
            MostrarInventario(inventario)
        elif opcion == "3":
            VenderProducto(inventario)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
