# 1. Dado o código Python abaixo, qual a complexidade assintótica no pior caso?
def funcao(n): #n(n+1)/2=> O(n^2)
    for i in range(n): # O(n)
        for _ in range(i, n): # n, n-1, n-2, n-3, ... ,0
            k = 0
            while k < 5:
                k += 1
                
# O(n) * n(n-1)/2 * 5 