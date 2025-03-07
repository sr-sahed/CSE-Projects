#include <iostream>
using namespace std;

// Class Definition
class Car
{
public:
    string brand;
    int year;

    void display()
    {
        cout << "Brand: " << brand << ", Year: " << year << endl;
    }
};

int main()
{
    Car car1; // Object Creation
    car1.brand = "Toyota";
    car1.year = 2022;
    car1.display();

    return 0;
}
