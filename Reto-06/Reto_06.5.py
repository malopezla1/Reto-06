def same_letters(lista):
    result = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if sorted(lista[i]) == sorted(lista[j]):
                if lista[i] not in result:
                    result.append(lista[i])
                if lista[j] not in result:
                    result.append(lista[j])
    return result

entrance = input("Ingresa las palabras separadas por comas: ")
lista_words = [palabra.strip() for palabra in entrance.split(',')]

print(f"Palabras con los mismos caracteres: {same_letters(lista_words)}")