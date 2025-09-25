import pdb
# Inventario de Redlash (Productos obligatorios en cada aplicación)

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

# Diccionarios con las medidas de los diseños
diseños = {
    "cat eye": [14, 13, 11, 10, 9, 8],
    "open eye": [13, 12, 10, 9],
    "natural": [12, 11, 10, 9, 8],
    "fox eye": [13, 12, 11, 10, 9, 8]
}
# Diccionario con las medidas que contiene cada blister de pestañas
aplicaciones = {
    "volumen griego": [14, 13, 12, 11, 10, 9, 8],
    "volumen hawaiiano": [14, 13, 12, 11, 10, 9, 8],
    "volumen": [14, 13, 12, 11, 10, 9],
    "efecto rimel": [14, 13, 12, 11, 10, 9, 8]
}

# Función de Registro de clientas, eleccion de aplicación, diseño y descontado de productos obligatorios

clientes = []

def registrar_cliente():
    print("\n--- Registro de nueva clienta ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    telefono = input("Número de teléfono: ")
    fecha = input("Fecha de aplicación (dd/mm/aaaa): ")
    
    while True:
        try:
            aplicacion = input("Introduce el nombre del tipo de aplicacion (Volumen, Volumen griego, Volumen hawaiiano, Efecto rimel): \t")
            aplicacion = aplicacion.strip().lower()
            if aplicacion in aplicaciones:
                usar_aplicacion(aplicacion)
                break
            else:
                print("Esta aplicacion no está registrada o se encuentra mal escrita. Intenta de nuevo \n")
        except Exception as e:
            print(f"Ocurrio un error: {e}. Intenta de nuevo \n")  
   
    while True:
        try:
            diseño = input("Introduce el nombre del diseño (Cat eye, Open eye, Natural, Fox eye): \t")
            diseño = diseño.strip().lower()
            if diseño in diseños:
                usar_diseño(diseño)
                break
            else:
                print("\nEste diseño no está registrado o se encuentra mal escrito. Intenta de nuevo \n")
        except Exception as e:
            print(f"Ocurrio un error: {e}. Intenta de nuevo \n")

    # Se llama a la funcion para descontar recursos obligatorios automáticamente al registrar la clienta
    recursos_obligatorios(inventario)

    cliente = {
        "nombre": nombre,
        "edad": edad,
        "fecha": fecha,
        "diseño": diseño,
        "tipo": aplicacion,
        "telefono": telefono
    }

    clientes.append(cliente)
    print(f" Cliente '{nombre}' registrado correctamente.")



def mostrar_clientes():
    print("\n Lista de clientes:")
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"\nCliente {i}:")
            for clave, valor in cliente.items():
                print(f"  {clave.capitalize()}: {valor}")

def recursos_obligatorios(inventario, sesiones=1):
    for i in range(sesiones):
        for item, datos in inventario.items():
            if datos["cantidad"] >= datos["uso"]:
                datos["cantidad"] -= datos["uso"]
            else:
                print(f" No hay suficiente inventario de {item}.")
    print ("\nSe han descontado los productos obligatorios\n")


#Funciones de los servicios

def usar_diseño(nombre_diseño):
    if nombre_diseño in diseños:
        print(f"Diseño seleccionado diseño: {nombre_diseño}")
        for medida in diseños[nombre_diseño]:
            usar_tiras(medida)
    else:
        print("Ese diseño no está registrado.")


def usar_aplicacion(nombre_aplicacion):
    if nombre_aplicacion in aplicaciones:
        print(f"Tipo de aplicación seleccionada: {nombre_aplicacion}")
        for medida in aplicaciones[nombre_aplicacion]:
            usar_tiras(medida)
    else:
        print("Ese diseño no está registrado.")


# Funciones de Inventario

def usar_tiras(medida, cantidad=1):
    if medida in medidas:
        if medidas[medida] >= cantidad:
            medidas[medida] -= cantidad
        else:
            print(f"No hay suficientes tiras de {medida}mm (quedan {medidas[medida]}).")
    else:
        print(f"La medida {medida}mm no existe en el inventario.")

def mostrar_inventario():
    print(" Inventario actual:")
    for producto, datos in inventario.items():
        print(f"- {producto}: {datos['cantidad']} {datos['unidad']} | Precio: ${datos['precio']}")

def mostrar_medidas():
    print("Inventario actual:")
    for medida, tiras in sorted(medidas.items(), reverse=True):
        print(f"Medida {medida}mm: {tiras} tiras")

def reabastecer():
    while True:
        producto_reabas = input( "Ingrese el producto que va reabastecer: ").strip().lower()
        if producto_reabas in inventario:
            cantidad_reabas = int(input( "Cuanto va reabastecer? "))
            inventario[producto_reabas]["cantidad"] += cantidad_reabas
            break
        else: 
            print ("No en el inventario")

#Funcion de reporte final
def generar_reporte_final(nombre_archivo="reporte_final.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("--- Inventario ---\n")
        f.write(f"{'Nombre':25} {'cantidad':>5} {'precio':>7} {'uso':>8}\n")
        f.write("-" * 65 + "\n")
        for nombre, datos in inventario.items():
            f.write(f"{nombre:25} {datos['cantidad']:>5} ${datos['precio']:>6} {str(datos['uso']):>8}\n")
        f.write("\n")

    print("Reporte final guardado como reporte_final.txt\n")



# Opciones de Menú

def mostrar_menu():
    print("--- Menú de operaciones ---")
    print ("1. Registrar Clienta")
    print ("2. Mostrar Clientas Registardos")
    print ("3. Usar tiras por medida")
    print ("4. Mostrar Inventario")
    print ("5. Reabastecer Inventario")
    print ("6. Crear Reporte Final")
    print ("7. Salir")
    return input("Elige una opción: \t")
    
    

# Añdir la funcion de descontar productos obligatorios al registro de clienta
# Añadir la funcion de reporte final

# Ejecución del menú


opcion = ""
while opcion!=7:
    opcion = mostrar_menu()

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        mostrar_clientes()
    elif opcion == "3":
        try:
            medida = int(input("Introduce la medida (8 - 14mm): \t"))
            usar_tiras(medida)
        except ValueError:
            print("Por favor, introduce un número entero.")
    elif opcion == "4":
        mostrar_inventario()
        mostrar_medidas()
    elif opcion == "5":
        reabastecer()
    elif opcion == "6":
        generar_reporte_final()
    elif opcion == "7":
        print("\nPrograma cancelado.\n")
    else:
        print("\n Opción no válida. Elige solo la opcion del 1 al 7.\n")


