def operaciones(num1: float, num2: float, operation: float) -> float | str:
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "¡Error!: No se puede dividir por 0."
    else:
        return "¡Error!: Operación no válida."

try:
    num1: float = int(input("Ingresa tu primer número: "))
    num2: float = int(input("Ingresa tu segundo número: "))
    print("\nSuma seleccione: 1 ")
    print("Resta seleccione: 2 ")
    print("Multiplicacion seleccione: 3 ")
    print("Division seleccione: 4 ")
    operation = int(input("\nSelecciona el tipo de operación: "))
except ValueError:
    print("¡Error!: Entrada no válida. Por favor ingresa números.")
else:
    print(operaciones(num1, num2, operation))
