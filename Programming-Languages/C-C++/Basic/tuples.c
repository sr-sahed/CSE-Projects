#include <stdio.h>

struct Tuple
{
    int x;
    float y;
    char z;
};

int main()
{
    struct Tuple t1 = {10, 3.14, 'A'};
    printf("Tuple values: %d, %.2f, %c\n", t1.x, t1.y, t1.z);
    return 0;
}
