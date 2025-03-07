#include <stdio.h>
#include <string.h>

struct Dictionary
{
    char key[50];
    int value;
};

int main()
{
    struct Dictionary dict[] = {{"apple", 1}, {"banana", 2}, {"cherry", 3}};

    for (int i = 0; i < 3; i++)
    {
        printf("Key: %s, Value: %d\n", dict[i].key, dict[i].value);
    }
    return 0;
}
