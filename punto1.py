#Ejercicio 1:
#Considera un algoritmo que toma como entrada un entero positivo n. Si n es par, el algoritmo
#lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y le suma uno. El
#algoritmo repite esto hasta que n sea uno. Por ejemplo, la secuencia para el valor 3 es la
#siguiente:
#3 ➝ 10 ➝ 5 ➝ 16 ➝ 8 ➝ 4 ➝ 2 ➝ 1

#Tu tarea es simular la ejecución del algoritmo para un valor dado de n.
#Input: El único parámetro de entrada contiene un entero n.
#Output: Retorna una línea que contenga todos los valores de n durante la ejecución del algoritmo.
#Constraints: 1 < n < 10


def simular_ejecucion(n):
    ans = []
    ans.append(n)
    while n!=1:
        if (n%2)==0:
         n=n//2
    else:
        n=n*3+1
        ans.append(n)

print(n)