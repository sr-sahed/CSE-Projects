#include <iostream>
using namespace std;

class Animal
{
public:
    void eat()
    {
        cout << "This animal eats food" << endl;
    }
};

class Dog : public Animal
{
public:
    void bark()
    {
        cout << "Dog barks" << endl;
    }
};

int main()
{
    Dog myDog;
    myDog.eat();
    myDog.bark();

    return 0;
}
