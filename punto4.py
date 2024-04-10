def convertir_palindrome(palabra):
    
    caracter_unicos = set(palabra) # ordena en un conjunto los caracteres unicos , osea elimina las letras que se repiten
    orden_letras = sorted(caracter_unicos, reverse=True) # ordena las letras de forma descendente (de mayor a menor) y devuelve una nueva lista con estos elementos ordenados
    
    palidromo_lista = [] # se crea una lista vacia para los valores del palindromo
    letra_impar = [] 
    # se crea un for que recorre cada letras en la lista "orden_letra"
    for letra in orden_letras:
        count = palabra.count(letra)  # y cuenta cuantas veces aparece esa letra en la cadena "palabra"
       
    # se verifica si el recuento de las letras es par o impar
        if count % 2 == 0: #verifica si el contador es par 
            #si es par entonces 
            for _ in range(count//2):
                # se inserta la letra  al principio y al final en la lista
                palidromo_lista.insert(0,letra)
                palidromo_lista.append(letra)
    
        else:
            # si es impar la letra se retorna esto
            if letra_impar:
                return 'NO SOLUTION' 
            
            palidromo_lista.insert(len(palidromo_lista) // 2,letra)
            letra_impar = True

    return ''.join(palidromo_lista) # une todas las letras sin separarlas

# caso de prueba
assert convertir_palindrome("aabbc") == "abcba", "Error en el caso de prueba"

print('todos los casos de pruba han pasado correctamente.')  