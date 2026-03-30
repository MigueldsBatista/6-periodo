import random
import time
from typing import Literal

def swap(arr: list[int], i: int, j: int):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


def insertionSort(arr: list[int]):
    start = time.perf_counter()
    
    for i in range(1, len(arr)):
        j=i
        while(arr[j] < arr[j-1] and j > 0):
            swap(arr, j, j -1)
            j-=1

    print("\n")
    
    end = time.perf_counter()
    return (end - start) * 1000


def linearSearch(arr: list, target):
    start = time.perf_counter()
    
    for index, el in enumerate(arr):
        if el == target:
            return (time.perf_counter() - start) * 1000

    return (time.perf_counter() - start) * 1000


def analyze_insertion():
    SIZE = 1000
    
    pior_caso = random_array(SIZE, 'reversed')
    melhor_caso = random_array(SIZE, 'ordered')
    caso_medio = random_array(SIZE, 'random')

    print('---------------------------------------')
    print('INSERTION SORT\n')
    print('Tamanho: ', SIZE)
    
    for label, caso in [('Pior Caso', pior_caso), ('Melhor Caso', melhor_caso), ('Caso Médio', caso_medio)]:
        tempo = insertionSort(caso)
        print(label)
        print(f"Tempo em ms: {tempo:2f}\n")
        
def analyze_linear() -> int:
    SIZE = 1000
    arr = random_array(SIZE, 'ordered')
    
    pior_caso = arr[-1]
    melhor_caso = arr[1]
    caso_medio = len(arr) - 1 // 2
    
    print('---------------------------------------')
    print('LINEAR SEARCH\n')
    
    print('Tamanho: ', SIZE)
    for label, caso in [
        ('Pior Caso', pior_caso), 
        ('Melhor Caso', melhor_caso), 
        ('Caso Médio', caso_medio)
    ]:
        tempo = linearSearch(arr, caso)
        print(label)
        print(f"Tempo em ms: {tempo:2f}\n")
        

def random_array(size: int, type: Literal['ordered' , 'reversed' , 'random']):
    arr = []
    if type == 'ordered':
        arr = [i for i in range(size)]
    elif type == 'reversed':
        arr = [i for i in range(size)][::-1]
    else:
        arr = [int(random.randint(1, size)) for _ in range(size)]
    
    return arr
    
        
analyze_insertion()
analyze_linear()