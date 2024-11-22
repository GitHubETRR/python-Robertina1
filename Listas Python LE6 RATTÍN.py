bailarines = []
puntajes = []
resultados = []

def registrar_bailarines():
    nombre = input("Ingrese el nombre del bailarin: \n")
    if nombre in bailarines:
        print(f"El bailarin '{nombre}' ya está dentro del competencia.")
    else:
        bailarines.append(nombre)
        puntajes.append(None)
        print(f"{nombre} ya fue agregado a la competencia.")
        

def agregar_puntaje():
    nombre = input("Ingrese el nombre del bailarin para agregar puntaje: \n")
    while True:  
        try:
            puntaje = int(input("Ingresa un puntaje (entre 0 y 10): "))
            if 0 <= puntaje <= 10:  
                indice = bailarines.index(nombre)
                puntajes[indice] = puntaje
                print(f"Se ingresó el puntaje {puntaje} para el bailarin {nombre}.")
                break  
            else:
                print("El puntaje debe estar entre 0 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

def mostrar_resultados():
    if not bailarines:
        print("No hay bailarines ingresados en la competencia.")
        return
    
    print("Lista de resultados:")
    for i in range(len(bailarines)):
        puntaje = puntajes[i] if puntajes[i] is not None else "Sin puntaje"
        print(f"{bailarines[i]}: {puntaje}")

    print("Resultados:")
    for resultado in resultados:
        print(resultado)

def mostrar_ganador():
    if all(i is None for i in puntajes):
        print("No se han asignado puntajes a ningún bailarín.")
        return
    
    max_puntaje = max(i for i in puntajes if i is not None) 
    indice_ganador = puntajes.index(max_puntaje)
    nombre_ganador = bailarines[indice_ganador]

    print(f"El ganador es {nombre_ganador} con un puntaje de {max_puntaje}. ¡Felicitaciones!")

def Menu():
    while True:
        print("Menú de competencia de baile")
        print("1.Registrar bailarin")
        print("2.Agregar puntaje a un bailarin")
        print("3.Mostrar la lista de resultados")
        print("4.Mostrar ganador")
        print("5.Salir")
        
        opcion = input("Selecciona una opcion (0-5)\n")
        if opcion == '1':
            registrar_bailarines()
        elif opcion == '2':
            agregar_puntaje()
        elif opcion == '3':
            mostrar_resultados()
        elif opcion == '4':
            mostrar_ganador()
        elif opcion == '5':
            print("Gracias por ser parte de la competencia.")
            break
        else:
            print("Esta opcion no esta dentro del menu de la competencia. Debe ser en el rango del (1-5).")
            
            
Menu()