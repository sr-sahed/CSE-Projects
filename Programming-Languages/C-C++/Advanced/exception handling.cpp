#include <iostream>
using namespace std;

void divide(int a, int b)
{
    try
    {
        if (b == 0)
            throw "Division by zero error!";
        cout << "Result: " << (a / b) << endl;
    }
    catch (const char *e)
    {
        cout << "Exception: " << e << endl;
    }
}

int main()
{
    divide(10, 2);
    divide(5, 0);
    return 0;
}
