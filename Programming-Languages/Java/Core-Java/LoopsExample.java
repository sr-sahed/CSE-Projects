public class LoopsExample {
    public static void main(String[] args) {
        // For Loop
        System.out.println("For Loop:");
        for (int i = 1; i <= 3; i++) {
            System.out.println("Iteration: " + i);
        }

        // While Loop
        System.out.println("While Loop:");
        int j = 1;
        while (j <= 3) {
            System.out.println("Iteration: " + j);
            j++;
        }

        // Do-While Loop
        System.out.println("Do-While Loop:");
        int k = 1;
        do {
            System.out.println("Iteration: " + k);
            k++;
        } while (k <= 3);
    }
}
