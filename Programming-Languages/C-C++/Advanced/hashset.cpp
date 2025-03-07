#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    unordered_set<int> uniqueNums = {1, 2, 3, 4, 5, 5, 3};

    cout << "Unique numbers: ";
    for (int n : uniqueNums)
        cout << n << " ";

    return 0;
}
