 #--- Blisters ---
blisters = {
    "Blister W": {
        "medidas": list(range(8, 15)),
        "tiras_por_medida": 2,
        "total_tiras": 12,
        "consumo_por_aplicacion": "1 tira por medida utilizada",
        "stock": 4,
        "precio": 141
    },
    "Blister YY": {
        "medidas": list(range(8, 15)),
        "tiras_por_medida": 2,
        "total_tiras": 12,
        "consumo_por_aplicacion": "1 tira por medida utilizada",
        "stock": 4,
        "precio": 135
    },
    "Blister Volumen": {
        "medidas": list(range(9, 15)),
        "tiras_por_medida": 3,
        "total_tiras": 18,
        "consumo_por_aplicacion": "Se usa TODO el blister",
        "stock": 4,
        "precio": 300
    },
    "Blister Clásicas": {
        "medidas": list(range(8, 15)),
        "tiras_por_medida": 2,
        "total_tiras": 12,
        "consumo_por_aplicacion": "1 tira por medida utilizada",
        "stock": 4,
        "precio": 100
    }
}

# --- Tipos de aplicación ---
aplicaciones = {
    "Volumen": "Blister Volumen",
    "Volumen Griego": "Blister W",
    "Volumen Hawaiiano": "Blister YY",
    "Efecto Rimel": "Blister Clásicas"
}

# --- Diseños ---
diseños = {
    "Cat eye": {
        "medidas": [14, 13, 11, 10, 9, 8],
        "gasto": "media tira"
    },
    "Open eye": {
        "medidas": [13, 12, 10, 9],
        "gasto": "media tira"
    },
    "Natural": {
        "medidas": [12, 11, 10, 9, 8],
        "gasto": "media tira"
    },
    "Fox eye": {
        "medidas": [13, 12, 11, 10, 9, 8],
        "gasto": "un cuarto de tira"
    }
}

# --- Materiales generales ---
materiales = {
    "Microbrush": {"contenido": "100 pzs", "uso": 1, "precio": 30, "stock": 1},
    "Lip Brush": {"contenido": "100 pzs", "uso": 1, "precio": 32, "stock": 1},
    "Cepillos": {"contenido": "50 pzs", "uso": 1, "precio": 36, "stock": 1},
    "Bonder": {"contenido": "15 ml", "uso": 0.15, "precio": 260, "stock": 1},
    "Pegamento": {"contenido": "5 ml", "uso": 0.10, "precio": 300, "stock": 1},
    "Anillos para pegamento": {"contenido": "25 pzs", "uso": 1, "precio": 65, "stock": 1},
    "Pads de microfibra": {"contenido": "200 pzs", "uso": 2, "precio": 210, "stock": 1},
    "Cubrebocas": {"contenido": "100 pzs", "uso": 1, "precio": 218, "stock": 1},
    "Guantes de latex": {"contenido": "100 pzs", "uso": 2, "precio": 200, "stock": 1},
    "Cinta Micropore": {"contenido": "9 metros", "uso": "30 cm", "precio": 40, "stock": 1}
}

# --- Funciones ---
def mostrar_blisters():
    print("--- Inventario de Blisters ---")
    for nombre, datos in blisters.items():
        print(f"{nombre}: {datos['stock']} disponibles, ${datos['precio']} c/u")

def mostrar_materiales():
    print("--- Materiales ---")
    for nombre, datos in materiales.items():
        print(f"{nombre}: {datos['stock']} paquete(s), precio ${datos['precio']}")

def mostrar_diseños():
    print("--- Diseños ---")
    for diseño, datos in diseños.items():
        print(f"{diseño}: medidas {datos['medidas']} - gasto {datos['gasto']}")

def mostrar_aplicaciones():
    print("--- Tipos de aplicación ---")
    for tipo, blister in aplicaciones.items():
        print(f"{tipo} - usa {blister}")

# --- Guardar inventario en TXT ---
def generar_reporte_final(nombre_archivo="reporte_final.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        # --- Blisters ---
        f.write("--- Inventario de Blisters ---\n")
        f.write(f"{'Nombre':20} {'Stock':>5} {'Precio':>7} {'Tiras por medida':>15} {'Total tiras':>12} {'Consumo':>25}\n")
        f.write("-" * 90 + "\n")
        for nombre, datos in blisters.items():
            f.write(f"{nombre:20} {datos['stock']:>5} ${datos['precio']:>6} {datos['tiras_por_medida']:>15} {datos['total_tiras']:>12} {datos['consumo_por_aplicacion']:>25}\n")
        f.write("\n")

        # --- Materiales ---
        f.write("--- Materiales ---\n")
        f.write(f"{'Nombre':25} {'Stock':>5} {'Contenido':>12} {'Precio':>7} {'Uso':>8}\n")
        f.write("-" * 65 + "\n")
        for nombre, datos in materiales.items():
            f.write(f"{nombre:25} {datos['stock']:>5} {datos['contenido']:>12} ${datos['precio']:>6} {str(datos['uso']):>8}\n")
        f.write("\n")

        # --- Diseños ---
        f.write("--- Diseños ---\n")
        f.write(f"{'Diseño':20} {'Medidas':30} {'Gasto':>12}\n")
        f.write("-" * 65 + "\n")
        for diseño, datos in diseños.items():
            medidas_str = ", ".join(map(str, datos['medidas']))
            f.write(f"{diseño:20} {medidas_str:30} {datos['gasto']:>12}\n")
        f.write("\n")

        # --- Aplicaciones ---
        f.write("--- Tipos de aplicación ---\n")
        f.write(f"{'Tipo de aplicación':25} {'Blister usado':25}\n")
        f.write("-" * 55 + "\n")
        for tipo, blister in aplicaciones.items():
            f.write(f"{tipo:25} {blister:25}\n")
        f.write("\n")

    print(f"Reporte final guardado en '{nombre_archivo}'")

# Ejecutar
generar_reporte_final("mi_reporte_final.txt")
