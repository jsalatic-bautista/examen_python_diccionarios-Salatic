personas = {}

while True:
    print(" BIENVENIDO AL MENU ")
    print("1. Cargar datos")
    print("2. Buscar por DNI")
    print("3. Buscar por nombre")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        dni = int(input("Ingrese el DNI: "))
        nombre = input("Ingrese el nombre: ")
        personas[dni] = nombre
        print("Persona cargada")

    elif opcion == "2":
        dni_buscado = int(input("Ingrese el DNI a buscar: "))
        if dni_buscado in personas:
            print(f"El DNI es {dni_buscado} y su nombre es: {personas[dni_buscado]}")
        else:
            print("DNI no encontrado")

    elif opcion == "3":
        nombre_buscado = input("Ingrese el nombre a buscar: ")
        for dni, nombre in personas.items(): 
            if nombre.lower() == nombre_buscado.lower():
                print(f"Nombre encontrado: {nombre} y DNI: {dni}")

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("¡ERROR!: Opción no valida")