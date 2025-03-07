#include <iostream>
using namespace std;

int main()
{
    auto add = [](int a, int b)
    { return a + b; };
    cout << "Sum: " << add(5, 3) << endl;
    return 0;
}
