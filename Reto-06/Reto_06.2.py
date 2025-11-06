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