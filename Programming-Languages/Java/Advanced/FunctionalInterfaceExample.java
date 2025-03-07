@FunctionalInterface
interface MyFunctionalInterface {
    void displayMessage(String msg);
}

public class FunctionalInterfaceExample {
    public static void main(String[] args) {
        MyFunctionalInterface obj = msg -> System.out.println("Message: " + msg);
        obj.displayMessage("Java Functional Interface!");
    }
}
