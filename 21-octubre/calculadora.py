import time

def mostrar_menu():
    print("\nSeleccionar la operación que deseas realizar: \n")
    print("1) Sumar")
    print("2) Restar")
    print("3) Salir")
    opcion = int(input("Ingrese su opción: "))
    return opcion

def sumar(n1, n2):
    resultado = n1 + n2
    print(f"El resultado de la suma es {resultado}")
    return resultado

def restar(n1,n2):
    resultado = n1 - n2
    print(f"El resultado de la resta es {resultado}")
    return resultado

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1 or opcion == 2:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            if opcion == 1:
                sumar(n1, n2)
                time.sleep(3)
            elif opcion == 2:
                restar(n1,n2)
                time.sleep(3)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú")


main()
#mostrar_menu()
#sumar(2,2)
#restar(3,1)