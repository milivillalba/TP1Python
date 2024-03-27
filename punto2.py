def missing_number(n):
    acc1=0
    acc2=0
    
    for i in 1:
        acc1= acc1+i
        for j in range(1,n+1):
            acc2=acc2+j
            return acc2-acc1
        print(missing_number(5,[1,2,4,5]))


assert  missing_number(5,[1,2,4,5])==3,"Error en el caso de prueba"


#return ((n*(n+1)//2)-sum(1))