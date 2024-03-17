def show_menu():
    print("""
** Calculadora **

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
""")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opción no válida. Ingrese un número entre 1 y 5")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero")

def main():
    while True:
        show_menu()
        opcion = obtener_opcion()
        resultado = 0

        number_one = int(input("Ingrese el primer número: "))
        number_two = int(input("Ingrese el segundo número: "))

        if opcion == 1:
            resultado = number_one + number_two
            print(f"{number_one} + {number_two} = {resultado}")
        elif opcion == 2:
            resultado = number_one - number_two
            print(f"{number_one} - {number_two} = {resultado}")
        elif opcion == 3:
            resultado = number_one * number_two
            print(f"{number_one} * {number_two} = {resultado}")
        elif opcion == 4:
            resultado = number_one / number_two
            print(f"{number_one} / {number_two} = {resultado}")
        elif opcion == 5:
            print("Saliendo del menú...")
            break

if __name__ == "__main__":
    main()