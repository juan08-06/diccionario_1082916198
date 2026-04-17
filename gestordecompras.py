lista_compras = []

def agregar_articulo():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    articulo = {'producto': nombre, 'precio': precio, 'cantidad': cantidad}
    lista_compras.append(articulo)
    print("Artículo agregado.")

def ver_lista():
    if not lista_compras:
        print("La lista está vacía.")
        return
    for articulo in lista_compras:
        for clave, valor in articulo.items():
            print(f"{clave}: {valor}")
        print("---")

def calcular_total():
    total = 0
    for articulo in lista_compras:
        total += articulo['precio'] * articulo['cantidad']
    print(f"Total: {total}")

def eliminar_articulo():
    nombre = input("Nombre del producto a eliminar: ")
    for articulo in lista_compras:
        if articulo['producto'] == nombre:
            lista_compras.remove(articulo)
            print("Artículo eliminado.")
            return
    print("Producto no encontrado.")

def main():
    while True:
        print("\n1. Agregar artículo")
        print("2. Ver lista de compras")
        print("3. Calcular total")
        print("4. Eliminar artículo")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_articulo()
        elif opcion == '2':
            ver_lista()
        elif opcion == '3':
            calcular_total()
        elif opcion == '4':
            eliminar_articulo()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
