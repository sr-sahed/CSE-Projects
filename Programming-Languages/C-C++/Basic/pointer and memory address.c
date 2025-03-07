#include <stdio.h>

int main()
{
    int num = 10;
    int *ptr = &num;

    printf("Value: %d\n", num);
    printf("Pointer Address: %p\n", ptr);
    return 0;
}
