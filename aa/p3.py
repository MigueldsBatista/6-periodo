def calcular(n):
    passos = 0
    i = n 
    
    while i > 1:
        i = i //2 
        passos += 1
    print(passos)
    return passos

calcular(100)
