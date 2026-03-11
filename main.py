#Primeras fases del codigo 
#Creacion del alfabeto 
alfabeto = ['A','J','V','E','D','S']


cadena = input("Ingresa la cadena de acciones separadas por espacio: ")

acciones = cadena.split()

#Excepcion cuando el usuario de una entrada incorrecta
for simbolo in acciones:
    if simbolo not in alfabeto:
        print("Error: símbolo no válido:", simbolo)
        exit()

print("\nInterpretación de la sesión:\n")

#El sistema interpreta la entrada de la cadena 
for simbolo in acciones:

    if simbolo == 'A':
        print("Abrir aplicación")

    elif simbolo == 'J':
        print("Jugar videojuego")

    elif simbolo == 'V':
        print("Ver videos")

    elif simbolo == 'E':
        print("Usar aplicación educativa")

    elif simbolo == 'D':
        print("Descanso del dispositivo")

    elif simbolo == 'S':
        print("Salir de la aplicación")