# --- Blisters ---
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
def guardar_inventario_txt(nombre_archivo="inventario.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("--- Inventario de Blisters ---\n")
        for nombre, datos in blisters.items():
            f.write(f"{nombre}: {datos['stock']} disponibles, ${datos['precio']} c/u\n")
        f.write("--- Tipos de aplicación ---\n")
        for tipo, blister in aplicaciones.items():
            f.write(f"{tipo} - usa {blister}\n")
        f.write("--- Diseños ---\n")
        for diseño, datos in diseños.items():
            f.write(f"{diseño}: medidas {datos['medidas']} - gasto {datos['gasto']}\n")
        f.write("--- Materiales ---\n")
        for nombre, datos in materiales.items():
            f.write(f"{nombre}: {datos['stock']} paquete(s), precio ${datos['precio']}\n")
    print(f"Inventario guardado en '{nombre_archivo}'")

guardar_inventario_txt("mi_inventario.txt")
