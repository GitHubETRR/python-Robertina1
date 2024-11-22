def calculadora_simple():
    num1 = int(input("Ingrese un número: \n"))
    print(f"Una vez ingresado el primer numero siendo {num1} vamos por el segundo.\n")
    
    num2 = int(input("Ingrese otro número: \n"))
    print(f"¡Bien! ya tenemos ingresado el primer y segundo numero {num2} para poder operar.\n")
    
    print("Ingrese + si desea realizar una suma")
    print("Ingrese - si desea realizar una resta")
    print("Ingrese M si desea realizar una multiplicación")
    print("Ingrese D si desea realizar una división")
    
    operacion = input("Seleccione una operación: ").strip()  
    
    print(f"Números ingresados: {num1}, {num2}. Operación seleccionada: {operacion}")

    if operacion == "+":
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == "-":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == "M":
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == "D":
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir por cero, por lo que no se puede realizar la operacion.")

if __name__ == "__main__":
    calculadora_simple()
