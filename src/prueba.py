#Informacion personal y de contacto


contador_clientes = 0
num_clientes = int(input("Cuantos clientes va a registrar? "))
while contador_clientes <= num_clientes:
    contador_clientes=contador_clientes+1
    print ("Registro de la persona: ", contador_clientes)

    cancelar = input("Deseas cancelar el registro? solo escribe tal cual(si/no): ")
    if cancelar == "si":
        print ("Registro cancelado")
        break
    else:    
       nombre = input("ingrese su nombre: ")
       edad = int(input("Ingrese su edad: "))
#Opciones de aplicación
    aplicacion_pestañas = ["volumen", "volumen griego", "volumen hawaiiano", "efecto rimmel"]
    while True:
        print ("Opciones de Aplicación de Pestañas")
        for opcion in aplicacion_pestañas:
            print (opcion)
        tecnica = input ("Elige la tecnica (escribelo tal como aparece): ")
        if tecnica in aplicacion_pestañas:
            break
        else:
            print ("Opcion incorrecta intenta de nuevo. \n")
#Tipo de diseño
    opciones_diseño = ["cat eye", "open eye", "natural", "fox eye"]
    while True:
        print ("Opciones de diseño: ")
        for opcion in opciones_diseño:
            print (opcion)
        diseño = input ("Elige el tipo de diseño (escribelo tal cual): ")
        if diseño in opciones_diseño:
            break
        else:
            print ("Opcion incorrecta. Intenta de nuevo. \n")
#Medidas
    if tecnica == ("volumen"):
        medidas = int(input("¿Qué medidas desea del 9-14? "))
        while medidas <= 8 or medidas >= 15:
            print("El numero dado no es valido, ingrese otro número: ")
            medidas = int(input("¿Qué medidas desea del 9-14? "))
        tiras = (medidas - 8) * 3
print(tiras)
