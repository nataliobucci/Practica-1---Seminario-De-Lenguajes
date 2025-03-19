import sys

inventario = [["leche", 10], ["pan", 5], [
    "queso", 15], ["jugo", 20], ["agua", 30]]

while (True):
    opcion = int(input("""Menu:
                    1: Agregar Producto.
                    2: Eliminar Producto.
                    3: Imprimir Inventario.
                    4: Salir.
                    """))

    match opcion:
        case 1:

            prod = input("Ingrese el producto a agregar: ")
            for i in range(len(inventario)):
                if inventario[i][0] == prod:
                    print("Este producto ya fue ingresado")
                    break
            else:
                cant = int(input("Ingrese la cantidad: "))
                inventario.append([prod, cant])
        case 2:
            prod = input("Ingrese el producto a eliminar: ")
            for e in range(len(inventario)):
                if inventario[e][0] == prod:
                    print("producto correctamente eliminado")
                    eliminado = True
                    inventario.pop(e)
                    break
            if (not eliminado):
                print("El producto ingresado no se encuentra en el inventario: ")
        case 3:
            for elem in inventario:
                print(elem)
        case 4:
            sys.exit(1)
