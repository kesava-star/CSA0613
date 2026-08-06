#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define SIZE 100000

int arr[SIZE];

typedef struct {
    int left;
    int right;
} ThreadData;

void merge(int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while (i < n1)
        arr[k++] = L[i++];

    while (j < n2)
        arr[k++] = R[j++];

    free(L);
    free(R);
}

void mergeSort(int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;

        mergeSort(left, mid);
        mergeSort(mid + 1, right);
        merge(left, mid, right);
    }
}

void *threadMergeSort(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    mergeSort(data->left, data->right);
    return NULL;
}

int main() {
    srand(time(NULL));

    for (int i = 0; i < SIZE; i++)
        arr[i] = rand() % 100000;

    ThreadData t1 = {0, SIZE / 2 - 1};
    ThreadData t2 = {SIZE / 2, SIZE - 1};

    pthread_t thread1, thread2;

    clock_t start = clock();

    pthread_create(&thread1, NULL, threadMergeSort, &t1);
    pthread_create(&thread2, NULL, threadMergeSort, &t2);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    merge(0, SIZE / 2 - 1, SIZE - 1);

    clock_t end = clock();

    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Parallel Merge Sort Completed Successfully.\n");
    printf("Execution Time: %.6f seconds\n", time_taken);

    return 0;
}



