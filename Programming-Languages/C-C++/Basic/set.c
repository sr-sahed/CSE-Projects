#include <stdio.h>

void printSet(int arr[], int size)
{
    printf("Set elements: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int set[] = {10, 20, 30, 40, 50}; // Set representation
    printSet(set, 5);
    return 0;
}
