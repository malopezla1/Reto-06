# Reto-06
En el siguiente reto se agregan las excepciones para el reto 1 y paquete shape del reto 5.

# Reto 06.1:
```python
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
```

# Reto 06.2:
```Python
def palindromo (word: str) -> bool:
    word = word.lower()
    inverted = ""
    for letter in word:
        inverted = letter + inverted
    return word == inverted

try:
    word = input("Ingrese una palabra: ")
    if not word:
        raise ValueError("Entrada vacía.")
    if not word.isalpha():
        raise ValueError("No es una palabra.")
    if palindromo(word):
        print("Es un palíndromo")
    else: 
        print("No es un palíndromo")
except Exception as e:
    print(f"¡Error!: {e}")
```

# Reto 06.3:
```Python
def result(num: int):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
lista = [1, "!", 3, 4, 5, 6, 7, 8, 9]
primos = []

for numero in lista:
    try:
        n = int(numero)                         
    except (TypeError, ValueError) as e:
        print(f"Elemento inválido en la lista: {numero!r} -> {e}")
        continue
    try:
        if result(n):
            primos.append(n)
    except Exception as e:
        print(f"Error procesando {numero!r}: {e}")

print(f"Estos son los numeros primos en la lista: {primos}")
```

# Reto 06.4:
```Python
def mayor_suma(lista_nums):
    if len(lista_nums) < 2:
        return None
    mayor = lista_nums[0] + lista_nums[1]
    for i in range(1, len(lista_nums) - 1):
        suma = lista_nums[i] + lista_nums[i + 1]
        if suma > mayor:
            mayor = suma
    return mayor

entrada_usuario = input("Ingresa los números de la lista separados por comas: ").strip()
if entrada_usuario == "":
    raise ValueError("No se ingresaron números.")

partes = [p.strip() for p in entrada_usuario.split(',')]
lista_nums = [int(numero) for numero in partes]   

print("La mayor suma de dos números consecutivos es:", mayor_suma(lista_nums))
```

# Reto 06.5
```Python
def same_letters(lista):
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista de palabras.")
    result = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            a = lista[i]
            b = lista[j]
            if not isinstance(a, str) or not isinstance(b, str):
                raise TypeError("Todos los elementos deben ser cadenas.")
            if sorted(a) == sorted(b):
                if a not in result:
                    result.append(a)
                if b not in result:
                    result.append(b)
    return result

entrance = input("Ingresa las palabras separadas por comas: ")
lista_words = [palabra.strip() for palabra in entrance.split(',')]

print(f"Palabras con los mismos caracteres: {same_letters(lista_words)}")
```

# Shape: 
La carpeta se encuentra subida aqui al repositorio, en resumen agrege excepciones para validar cuando no se ingresa un número o si ese número no cumple con las condiciones que se plantean como por ejemplo un lado negativo.
