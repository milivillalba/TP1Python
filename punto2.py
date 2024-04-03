
#"n" representa el rango maximo de los numeros de lista 
# "digitos" es la lista de numero en la que uno deve faltar 
def encontrar_numero_faltantes(n, digitos):
    try:
        lista_de_iteracion = set(range(1, n + 1)) # genera un conjunto de numeros que va del 1 al n, con set convertimos los num en conjunto
        numeros_ejemplos= set(digitos)
        numero_faltantes= lista_de_iteracion - numeros_ejemplos # utilizo "-" para encontra los elem que estan en la lista_de_iteracion pero no estan en los numeros_ejemplo , donde esto nos dara los numeros faltantes.
        return  numero_faltantes.pop() #extrae el elemento faltante  con el pop y lo devuelve como resultado
    except:
        return "error al realizar la busqueda del numero faltante"
    
print(encontrar_numero_faltantes(5,[1,2,4,5]))

assert encontrar_numero_faltantes(5,[1,2,4,5]) == 3,"Error en el caso de prueba"