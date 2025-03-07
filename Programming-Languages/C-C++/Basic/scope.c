#include <stdio.h>

int globalVar = 10; // Global scope

void testScope()
{
    int localVar = 20; // Local scope
    printf("Local variable: %d\n", localVar);
}

int main()
{
    testScope();
    printf("Global variable: %d\n", globalVar);
    return 0;
}
