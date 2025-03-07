#include <iostream>
using namespace std;

class Animal
{
public:
    virtual void makeSound()
    {
        cout << "Animal makes sound" << endl;
    }
};

class Dog : public Animal
{
public:
    void makeSound() override
    {
        cout << "Dog barks" << endl;
    }
};

int main()
{
    Animal *a;
    Dog d;
    a = &d;
    a->makeSound(); // Calls Dog's makeSound()

    return 0;
}
