#include <iostream>
using namespace std;

class IShape
{ // Interface
public:
    virtual void draw() = 0;
};

class Square : public IShape
{
public:
    void draw() override
    {
        cout << "Drawing a Square" << endl;
    }
};

int main()
{
    Square s;
    s.draw();

    return 0;
}
