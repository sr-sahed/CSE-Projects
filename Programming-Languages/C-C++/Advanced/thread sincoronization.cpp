#include <iostream>
#include <thread>
#include <mutex>
using namespace std;

mutex mtx;

void printNumber(int num)
{
    mtx.lock();
    cout << "Number: " << num << endl;
    mtx.unlock();
}

int main()
{
    thread t1(printNumber, 1);
    thread t2(printNumber, 2);

    t1.join();
    t2.join();
    return 0;
}
