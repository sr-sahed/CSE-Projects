#include <iostream>
#include <vector>
#include <list>
using namespace std;

int main()
{
    vector<int> arrList = {1, 2, 3, 4, 5};
    list<int> linkedList = {10, 20, 30, 40};

    cout << "ArrayList (Vector): ";
    for (int n : arrList)
        cout << n << " ";

    cout << "\nLinkedList (List): ";
    for (int n : linkedList)
        cout << n << " ";

    return 0;
}
