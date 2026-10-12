def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def potencia(a, b):
    return a ** b

def main():
    while True:
        print("\n=== Calculadora Sencilla ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ").strip()
        
        if opcion == "6":
            print("¡Hasta luego!")
            break
            
        if opcion not in {"1", "2", "3", "4", "5"}:
            print("Opción no válida. Intenta de nuevo.")
            continue
            
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor ingresa números válidos.")
            continue
            
        if opcion == "1":
            print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == "4":
            resultado = dividir(num1, num2)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"Resultado: {num1} / {num2} = {resultado}")
        elif opcion == "5":
            print(f"Resultado: {num1} ^ {num2} = {potencia(num1, num2)}")

if __name__ == "__main__":
    main()
