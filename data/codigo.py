import pdb
# Inventario de RedSlash

inventario = {
    "microbrush": {"cantidad": 100, "uso": 1, "precio": 30, "unidad": "pieza"},
    "lip Brush": {"cantidad": 100, "uso": 1, "precio": 32, "unidad": "pieza"},
    "cepillos": {"cantidad": 50, "uso": 1, "precio": 36, "unidad": "pieza"},
    "bonder": {"cantidad": 15, "uso": 0.15, "precio": 260, "unidad": "mililitros"},
    "pegamento": {"cantidad": 5, "uso": 0.15, "precio": 300, "unidad": "mililitros"},
    "anillos para pegamento": {"cantidad": 25, "uso": 1, "precio": 65, "unidad": "pieza"},
    "pads de microfibra": {"cantidad": 200, "uso": 2, "precio": 210, "unidad": "pieza"},
    "cubrebocas": {"cantidad": 100, "uso": 1, "precio": 218, "unidad": "pieza"},
    "guantes de latex": {"cantidad": 100, "uso": 2, "precio": 200, "unidad": "pieza"},
    "cinta micropore": {"cantidad": 9, "uso": 0.30, "precio": 40, "unidad": "metros"},
}

medidas = {medida: 3 for medida in range(8, 15)}

# Servicios predeterminados
diseños = {
    "cat eye": [14, 13, 11, 10, 9, 8],
    "open eye": [13, 12, 10, 9],
    "natural": [12, 11, 10, 9, 8],
    "fox eye": [13, 12, 11, 10, 9, 8]
}
aplicaciones = {
    "volumen griego": [14, 13, 12, 11, 10, 9, 8],
    "volumen hawaiiano": [14, 13, 12, 11, 10, 9, 8],
    "volumen": [14, 13, 12, 11, 10, 9],
    "efecto rimel": [14, 13, 12, 11, 10, 9, 8]
}

# Funciones
def mostrar_inventario():
    print(" Inventario actual:")
    for producto, datos in inventario.items():
        print(f"- {producto}: {datos['cantidad']} {datos['unidad']} | Precio: ${datos['precio']}")


def agregar_producto():
    nombre = input("\nIngresa el nombre del nuevo producto: ")
    cantidad = int(input("Cantidad inicial: "))
    precio = int(input("Precio: "))
    unidad = input("Unidad (pzs, ml, metros, etc.): ")
    inventario[nombre] = {"cantidad": cantidad, "precio": precio, "unidad": unidad}
    print(f" Producto '{nombre}' agregado correctamente.")


def usar_producto():
    nombre = input("\nIngresa el nombre del producto que quieres usar: ")
    if nombre in inventario:
        cantidad_usada = int(input("¿Cuánto deseas usar?: "))
        if cantidad_usada <= inventario[nombre]["cantidad"]:
            inventario[nombre]["cantidad"] -= cantidad_usada
            print(f" Se usaron {cantidad_usada} {inventario[nombre]['unidad']} de '{nombre}'.")
        else:
            print(" No hay suficiente stock disponible.")
    else:
        print(" El producto no existe en el inventario.")


def recursos_obligatorios(inventario, sesiones=1):
    for i in range(sesiones):
        for item, datos in inventario.items():
            if datos["cantidad"] >= datos["uso"]:
                datos["cantidad"] -= datos["uso"]
            else:
                print(f" No hay suficiente inventario de {item}.")
    print ("\nSe han descontado los productos obligatorios\n")


def reabastecer():
    while True:
        producto_reabas = input( "Ingrese el productor que va reabastecer: ").strip().lower()
        if producto_reabas in inventario:
            cantidad_reabas = int(input( "Cuanto va reabastecer? "))
            inventario[producto_reabas]["cantidad"] += cantidad_reabas
            break
        else: 
            print ("No en el inventario")


#Funciones de los sevicios
def mostrar_medidas():
    print("Inventario actual:")
    for medida, tiras in sorted(medidas.items(), reverse=True):
        print(f"Medida {medida}mm: {tiras} tiras")


def usar_tiras(medida, cantidad=1):
    if medida in medidas:
        if medidas[medida] >= cantidad:
            medidas[medida] -= cantidad
        else:
            print(f"No hay suficientes tiras de {medida}mm (quedan {medidas[medida]}).")
    else:
        print(f"La medida {medida}mm no existe en el inventario.")


def usar_diseño(nombre_diseño):
    if nombre_diseño in diseños:
        print(f"Aplicando diseño: {nombre_diseño}")
        for medida in diseños[nombre_diseño]:
            usar_tiras(medida)
    else:
        print("Ese diseño no está registrado.")


def usar_aplicacion(nombre_aplicacion):
    if nombre_aplicacion in aplicaciones:
        print(f"Aplicando diseño: {nombre_aplicacion}")
        for medida in aplicaciones[nombre_aplicacion]:
            usar_tiras(medida)
    else:
        print("Ese diseño no está registrado.")


def mostrar_menu():
    print("--- Menú de operaciones ---")
    print("1. Mostrar inventario")
    print("2. Usar tiras por medida")
    print("3. Usar diseño predeterminado")
    print("4. Usar tipo de aplicacion predeterminado")
    print("5. Reabastecer inventario")
    print("6. Descontado de productos obligatorios")
    print("7. Salir")
    return input("Elige una opción: \t")
#Funciones del inventario

# Programa principal
opcion = ""
while opcion!=7:
    opcion = mostrar_menu()

    if opcion == "1":
        mostrar_inventario()
        mostrar_medidas()

    elif opcion == "2":
        try:
            medida = int(input("Introduce la medida (8 - 14mm): \t"))
            usar_tiras(medida)
        except ValueError:
            print("Por favor, introduce un número válido.")

    elif opcion == "3":
        while True:
            try:
                diseño = input("Introduce el nombre del diseño (Cat eye, Open eye, Natural, Fox eye): \t")
                diseño = diseño.strip().lower()
                if diseño in diseños:
                    usar_diseño(diseño)
                    break
                else:
                    print ("\nEste diseño no está registrado o se encuentra mal escrito. Intenta de nuevo \n")
            except Exception as e:
                print (f"Ocurrio un error: {e}. Intenta de nuevo \n")

    elif opcion == "4":
        while True:
            try:
                aplicacion = input("Introduce el nombre del tipo de aplicacion (Volumen, Volumen griego, Volumen hawaiiano, Efecto rimel): \t")
                aplicacion = aplicacion.strip().lower()
                if aplicacion in aplicaciones:
                    usar_aplicacion(aplicacion)
                    break
                else:
                    print ("Esta aplicacion no está registrada o se encuentra mal escrita. Intenta de nuevo \n")
            except Exception as e:
              print (f"Ocurrio un error: {e}. Intenta de nuevo \n")  

    elif opcion == "5":
        reabastecer()
    elif opcion == "6":
        recursos_obligatorios(inventario)
    elif opcion == "7":
        print("Programa cancelado.")
    else:
        print("Opción no válida. Elige del 1 al 7.")
    control+=1
