directorio = {}

def agregar_contacto():
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    ciudad = input("Ciudad: ")
    directorio[nombre] = {'email': email, 'telefono': telefono, 'ciudad': ciudad}
    print("Contacto agregado.")

def ver_contactos():
    if not directorio:
        print("No hay contactos.")
        return
    for nombre, datos in directorio.items():
        print(f"Nombre: {nombre}")
        for clave, valor in datos.items():
            print(f"  {clave}: {valor}")
        print("---")

def buscar_por_nombre():
    nombre = input("Nombre a buscar: ")
    contacto = directorio.get(nombre)
    if contacto:
        print(f"Nombre: {nombre}")
        for clave, valor in contacto.items():
            print(f"  {clave}: {valor}")
    else:
        print("Contacto no encontrado.")

def actualizar_telefono():
    nombre = input("Nombre del contacto: ")
    if nombre in directorio:
        nuevo_telefono = input("Nuevo teléfono: ")
        directorio[nombre]['telefono'] = nuevo_telefono
        print("Teléfono actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Nombre a eliminar: ")
    if directorio.pop(nombre, None):
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")

def main():
    while True:
        print("\n1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar por nombre")
        print("4. Actualizar teléfono")
        print("5. Eliminar contacto")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            buscar_por_nombre()
        elif opcion == '4':
            actualizar_telefono()
        elif opcion == '5':
            eliminar_contacto()
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
