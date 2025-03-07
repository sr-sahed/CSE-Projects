class BankAccount {
    private double balance; // Private variable (Encapsulation)

    // Getter
    public double getBalance() {
        return balance;
    }

    // Setter
    public void setBalance(double amount) {
        if (amount >= 0) {
            balance = amount;
        }
    }
}

public class EncapsulationExample {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount();
        acc.setBalance(5000);
        System.out.println("Balance: " + acc.getBalance());
    }
}
