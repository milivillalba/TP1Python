#
# def comprobar_palindromo(palabra):
#     palabra= palabra.lower() #lower para convertir la palabra que ingreses en minuscula
#     palabra_invertido= palabra == palabra[::-1] #retorna la palabra con la vercion invertidad de derecha a izquierda
#     if palabra==palabra_invertido:
#      return palabra
    
# print(comprobar_palindromo("oso"))

def comprobar_palindromo(caracteres):
    convertir_minuscula= caracteres.lower()
    lista_palabras= convertir_minuscula.split()
    
    lista_sin_espacios=[]

    for palabra in lista_palabras:
        limpiar= palabra.strip(".").strip(",")
        lista_sin_espacios.append(limpiar)
        unir_cadena= "".join(lista_sin_espacios)
    # Generar todas las subcadenas
    subcadenas = []
    for i in range(len(unir_cadena)):
        for j in range(i + 1, len(unir_cadena) + 1):
            subcadenas.append(unir_cadena[i:j])

    # Comprobar si las subcadenas son palíndromos
    palindromos = []
    for subcadena in subcadenas:
        es_palindromo = True
        for i in range(len(subcadena) // 2):
            if subcadena[i] != subcadena[len(subcadena) - 1 - i]:
                es_palindromo = False
                break
        if es_palindromo:
            palindromos.append(subcadena)

    # Imprimir los palíndromos encontrados
    for palindromo in palindromos:
        print(palindromo)


print(comprobar_palindromo("hola como estas ana yo tengo un oso"))