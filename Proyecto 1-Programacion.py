nombre=input('¿Cómo te llamas? ')
edad=int(input('¿Cuál es tu edad '))
servicio=input('Escriba "aplicacion" si desea un tipo de aplicacion y "diseño" si desea un tipo de diseño ')
blister=''
tiras=0
if servicio=='aplicacion':
    aplicacion=input('¿Qué tipo de aplicacion desea?(Volumen, Volumen griego, Volumen hawaiiano, Efecto rimmel)'/t)
    if aplicacion=='Volumen':
        blister='volumen'
        medidas=int(input('¿Qué medidas desea del 9-14? '))
        while medidas<=8 or medidas>=15:
            print("El numero dado no es valido, ingrese otro numero")
            medidas=int(input('¿Qué medidas desea del 9-14? '))
        tiras=(medidas-8)*3
print(tiras)