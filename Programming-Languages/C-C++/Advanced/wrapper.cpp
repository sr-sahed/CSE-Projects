#include <iostream>
using namespace std;

int main()
{
    int num = 10;
    float wrappedNum = static_cast<float>(num);

    cout << "Wrapped Number: " << wrappedNum << endl;
    return 0;
}
