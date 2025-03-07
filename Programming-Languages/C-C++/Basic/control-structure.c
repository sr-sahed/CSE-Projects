#include <stdio.h>

int main()
{
    int num = 10;

    // If-else statement
    if (num > 0)
    {
        printf("Number is positive\n");
    }
    else
    {
        printf("Number is negative\n");
    }

    // Switch case
    switch (num)
    {
    case 10:
        printf("Number is 10\n");
        break;
    default:
        printf("Number is not 10\n");
    }

    return 0;
}
