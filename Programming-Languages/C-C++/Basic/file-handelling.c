#include <stdio.h>

int main()
{
    FILE *file = fopen("example.txt", "w");
    fprintf(file, "Hello, File Handling in C!");
    fclose(file);
    return 0;
}
