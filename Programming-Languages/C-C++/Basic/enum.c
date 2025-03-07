#include <stdio.h>

enum Days
{
    SUN,
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT
};

int main()
{
    enum Days today = WED;
    printf("Today is: %d\n", today);
    return 0;
}
