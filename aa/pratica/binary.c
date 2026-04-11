#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int binary_search(int *arr, int target, int start, int end){

    if(start > end)
        return -1;
    
    int mid_idx = (start + end) / 2;
    int mid_val = arr[mid_idx];

    if(mid_val == target)
        return mid_idx;
    
    if(target < mid_val)
        return binary_search(arr, target, start, mid_idx-1);
    else
        return binary_search(arr, target, mid_idx+1, end);
}


void insertion_sort(int *arr, int N){
    for (int i = 1; i < N; i++){
        int j = i;

        while (arr[j] < arr[j - 1] && j > 0){
            int temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j--;
        }
    }
}

int* random_arr(int size) {
    int *arr = (int*)malloc(sizeof(int) * size);

    // Inicializa a semente do gerador de números aleatórios
    srand(time(0));

    // Gera 10 números aleatórios entre 0 e 100
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 101; // Gera números de 0 a 100
    }

    return arr;
}

int main() {
    int size = 10, target;
    int *arr = random_arr(size);
    insertion_sort(arr, size);

    printf("\nValores gerados:\n");
    for (int i = 0; i < size; i++){
        printf("[%d] ->", arr[i]);
    }
    printf("\n");
    
    printf("Digite o valor para buscar: ");
    scanf("%d", &target);
    int index = binary_search(arr, target, 0, size - 1);
    printf("Index: %d", index);
    return 0;
}