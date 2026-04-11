#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *arr, int i, int j){
    int temp = arr[j];
    arr[j] = arr[i];
    arr[i] = temp;
}

void insertion_sort(int *arr, int N){
    // começamos do segundo elemento e vamos comparando ele com os anteriores
    
    for (int i = 1; i < N; i++){
        int j = i;

        while (arr[j] < arr[j - 1] && j > 0){
            swap(arr, j, j-1);
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
        printf("[%d] ->", arr[i]);
    }
    printf("\n");
    return arr;
}

int main() {
    int size = 10;
    int *arr = random_arr(size);
    insertion_sort(arr, size);
    printf("\nValores ordenados:\n");
    
    for (int i = 0; i < size; i++){
        printf("[%d] ->", arr[i]);
    }
    printf("\n");
    
    return 0;
}