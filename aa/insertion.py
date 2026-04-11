def swap(arr: list[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]

def insertion(arr: list[int]):
    for i in range(1, len(arr)):
        j=i
        
        while(arr[j] < arr[j-1] and j > 0):
            swap(arr, j, j -1)
            j-=1

arr = list(range(6))
insertion(arr)
print(arr)