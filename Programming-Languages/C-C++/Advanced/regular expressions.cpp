#include <iostream>
#include <regex>
using namespace std;

int main()
{
    string text = "Email: test@example.com";
    regex pattern("(\\w+@[a-zA-Z_]+?\\.[a-zA-Z]{2,6})");

    if (regex_search(text, pattern))
        cout << "Valid Email Found!" << endl;
    else
        cout << "No Valid Email!" << endl;

    return 0;
}
