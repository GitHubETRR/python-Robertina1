registro = {}

def mostrar_registro ():
    print("\nRegistro actual de las frutas en la verduleria.\n")
    for fruta, cantidad in registro.items():
        print(f"{fruta} : {cantidad} unidades\n")
    
def agregar_fruta ():
    fruta= input("Ingresar nombre de la fruta que desea: ")
    cantidad= int(input("Ingresar la cantidad de la fruta que deseo: "))
    
    fruta in registro
    if registro.get(fruta):
        registro[fruta]+= cantidad
    else:
        registro[fruta]=cantidad
        print(f"\n{cantidad} unidades de {fruta} agregadas al registro.\n ")
        
def calcular_total ():
    total= sum(registro.values())
    print(f"\nEl total registro de frutas es: {total} unidades\n")

while True:
    print("Menú de registro de frutas")
    print("1. Mostrar registro")
    print("2. Agregar fruta")
    print("3.Calcular el total de frutas")
    print("4. Salir")

    opcion = input("Seleccionar una opcion (1-4): ")
    
    if opcion == '1':
        mostrar_registro()
    elif opcion == '2':
        agregar_fruta()
    elif opcion == '3':
        calcular_total()
    elif opcion == '4':
        print("¡Gracias por chequear el registro de frutas de la verduleria!")
        break
    else:
        print("Esa opcion no se encuentra en el menú, seleccione una opcion (1-4) e intentalo de nuevo. \n")
