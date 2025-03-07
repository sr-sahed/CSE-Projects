#include <stdio.h>

// Function with parameters
int add(int a, int b)
{
    return a + b;
}

// Recursive function
int factorial(int n)
{
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

int main()
{
    printf("Addition: %d\n", add(5, 3));
    printf("Factorial: %d\n", factorial(5));
    return 0;
}
