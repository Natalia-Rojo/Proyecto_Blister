# Inventario inicial(del 8 al 14, cada medida con 3 tiras)
inventario = {medida: 3 for medida in range(8, 15)}

# Diseños predeterminados
diseños = {
    "cat eye": [14, 13, 11, 10, 9, 8],
    "open eye": [13, 12, 10, 9],
    "natural": [12, 11, 10, 9, 8],
    "fox eye": [13, 12, 11, 10, 9, 8]
}

# Funciones
def mostrar_inventario():
    print("Inventario actual:")
    for medida, tiras in sorted(inventario.items(), reverse=True):
        print(f"Medida {medida}mm: {tiras} tiras")

def usar_tiras(medida, cantidad=1):
    if medida in inventario:
        if inventario[medida] >= cantidad:
            inventario[medida] -= cantidad
        else:
            print(f"No hay suficientes tiras de {medida}mm (quedan {inventario[medida]}).")
    else:
        print(f"La medida {medida}mm no existe en el inventario.")

def usar_diseño(nombre_diseño):
    if nombre_diseño in diseños:
        print(f"Aplicando diseño: {nombre_diseño}")
        for medida in diseños[nombre_diseño]:
            usar_tiras(medida)
    else:
        print("Ese diseño no está registrado.")

def mostrar_menu():
    print("--- Menú de operaciones ---")
    print("1. Mostrar inventario")
    print("2. Usar tiras por medida")
    print("3. Usar diseño predeterminado")
    print("4. Salir")
    return input("Elige una opción: ")

# Programa principal
opcion = ""
while opcion != "4":
    opcion = mostrar_menu()

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        try:
            medida = int(input("Introduce la medida (8-14mm): "))
            usar_tiras(medida)
        except ValueError:
            print("Por favor, introduce un número válido.")
    elif opcion == "3":
        diseño = input("Introduce el nombre del diseño (cat eye, open eye, natural, fox eye): ").strip().lower()
        usar_diseño(diseño)
    elif opcion == "4":
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Elige del 1 al 4.")


# Se va adescontar lo que se usa en cada aplicacion obligatoriamente

def recursos_obligatorios(inventario, sesiones=1):
    for i in range(sesiones):
        for item, datos in inventario.items():
            if datos["stock"] >= datos["uso"]:
                datos["stock"] -= datos["uso"]
            else:
                print(f" No hay suficiente stock de {item}.")
    