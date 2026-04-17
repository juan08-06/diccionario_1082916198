lista = [12, 45, 78, 23, 56, 89, 34, 67]

def buscar_numero(numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
    return -1

def promedio_lista():
    if not lista:
        return 0
    return sum(lista) / len(lista)

def numeros_mayores(umbral):
    return [num for num in lista if num > umbral]

def ordenar_lista():
    return sorted(lista)

def main():
    while True:
        print("\nLista actual:", lista)
        print("1. Buscar número")
        print("2. Calcular promedio")
        print("3. Números mayores que um umbral")
        print("4. Ordenar lista")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            numero = int(input("Número a buscar: "))
            indice = buscar_numero(numero)
            if indice != -1:
                print(f"El número {numero} está en el índice {indice}.")
            else:
                print(f"El número {numero} no se encuentra en la lista.")
        elif opcion == '2':
            promedio = promedio_lista()
            print(f"El promedio de la lista es: {promedio}")
        elif opcion == '3':
            umbral = int(input("Umbral: "))
            mayores = numeros_mayores(umbral)
            print(f"Números mayores que {umbral}: {mayores}")
        elif opcion == '4':
            ordenada = ordenar_lista()
            print(f"Lista ordenada: {ordenada}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
