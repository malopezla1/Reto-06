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