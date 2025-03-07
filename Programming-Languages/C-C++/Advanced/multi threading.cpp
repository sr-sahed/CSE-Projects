#include <iostream>
#include <thread>
using namespace std;

void printMessage()
{
    cout << "Thread is running!" << endl;
}

int main()
{
    thread t(printMessage);
    t.join(); // Wait for the thread to finish
    return 0;
}
