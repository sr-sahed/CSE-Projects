#include <stdio.h>

int main()
{
    int list[] = {10, 20, 30, 40, 50}; // Array as list
    int size = sizeof(list) / sizeof(list[0]);

    printf("List elements: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");
    return 0;
}
