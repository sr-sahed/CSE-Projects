#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> nums = {5, 2, 8, 1, 9};

    sort(nums.begin(), nums.end()); // Ascending sort

    cout << "Sorted List: ";
    for (int n : nums)
        cout << n << " ";

    return 0;
}
