public class ControlStatementsExample {
    public static void main(String[] args) {
        int num = 10;
        if (num > 0) {
            System.out.println("Positive");
        } else {
            System.out.println("Negative");
        }

        int day = 2;
        switch (day) {
            case 1 -> System.out.println("Sunday");
            case 2 -> System.out.println("Monday");
            default -> System.out.println("Invalid day");
        }
    }
}
