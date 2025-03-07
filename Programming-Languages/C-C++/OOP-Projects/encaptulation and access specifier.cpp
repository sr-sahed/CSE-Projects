#include <iostream>
using namespace std;

class BankAccount
{
private:
    double balance;

public:
    BankAccount(double b) { balance = b; }

    void deposit(double amount)
    {
        balance += amount;
    }

    double getBalance()
    {
        return balance;
    }
};

int main()
{
    BankAccount myAccount(1000.50);
    myAccount.deposit(500);
    cout << "Current Balance: $" << myAccount.getBalance() << endl;

    return 0;
}
