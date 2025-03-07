class Counter {
    static int count = 0; // Static variable

    Counter() {
        count++;
    }

    static void showCount() {
        System.out.println("Count: " + count);
    }
}

public class StaticExample {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.showCount(); // Static method call
    }
}
