#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<string, int> scores;
    scores["Alice"] = 90;
    scores["Bob"] = 85;
    scores["Charlie"] = 95;

    for (auto &it : scores)
        cout << it.first << " => " << it.second << endl;

    return 0;
}
