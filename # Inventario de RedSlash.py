# Inventario de RedSlash

inventario = {
    "Microbrush": {"cantidad": 100, "precio": 30, "unidad": "pieza"},
    "Lip Brush": {"cantidad": 100, "precio": 32, "unidad": "pieza"},
    "Cepillos": {"cantidad": 50, "precio": 36, "unidad": "pieza"},
    "Bonder": {"cantidad": 15, "precio": 260, "unidad": "mililitros"},
    "Pegamento": {"cantidad": 5, "precio": 300, "unidad": "mililitros"},
    "Anillos para pegamento": {"cantidad": 25, "precio": 65, "unidad": "pieza"},
    "Pads de microfibra": {"cantidad": 200, "precio": 210, "unidad": "pieza"},
    "Cubrebocas": {"cantidad": 100, "precio": 218, "unidad": "pieza"},
    "Guantes de latex": {"cantidad": 100, "precio": 200, "unidad": "pieza"},
    "Cinta Micropore": {"cantidad": 9, "precio": 40, "unidad": "metros"},
}


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



def reabastecer():
    while True:
        producto_reabas = input( "Ingrese el productor que va reabastecer: ")
        if producto_reabas in inventario:
            cantidad_reabas = int(input( "Cuanto va reabastecer? "))
            inventario[producto_reabas]["cantidad"] += cantidad_reabas
            break
        else: 
            print ("No en el inventario")



while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Usar producto")
    print("4. Reabastecer Producto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        usar_producto()
    elif opcion == "4":
        reabastecer()
    elif opcion == "5":
        print(" Saliendo del sistema de inventario...")
        break
    else:
        print(" Opción no válida, intenta de nuevo.")
