#include <stdio.h>

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};     // 1D array
    int mat[2][2] = {{1, 2}, {3, 4}}; // 2D array

    printf("1D Array: %d\n", arr[2]);
    printf("2D Array: %d\n", mat[1][1]);

    return 0;
}
