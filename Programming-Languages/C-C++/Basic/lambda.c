#include <stdio.h>

int add(int a, int b) { return a + b; }

int main()
{
    int (*lambda)(int, int) = add;
    printf("Lambda function output: %d\n", lambda(3, 7));
    return 0;
}
