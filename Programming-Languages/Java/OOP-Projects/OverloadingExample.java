class MathOperations {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}

public class OverloadingExample {
    public static void main(String[] args) {
        MathOperations obj = new MathOperations();
        System.out.println("Addition (int): " + obj.add(5, 10));
        System.out.println("Addition (double): " + obj.add(5.5, 10.5));
    }
}
