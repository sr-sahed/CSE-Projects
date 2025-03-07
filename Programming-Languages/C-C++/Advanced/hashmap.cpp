#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<string, int> marks;
    marks["Alice"] = 90;
    marks["Bob"] = 85;
    marks["Charlie"] = 92;

    for (auto it : marks)
        cout << it.first << " => " << it.second << endl;

    return 0;
}
