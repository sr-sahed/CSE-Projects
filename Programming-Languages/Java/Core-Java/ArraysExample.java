public class ArraysExample {
    public static void main(String[] args) {
        // 1D Array
        int[] arr1D = { 10, 20, 30 };
        System.out.println("1D Array:");
        for (int num : arr1D)
            System.out.print(num + " ");

        // 2D Array
        int[][] arr2D = { { 1, 2 }, { 3, 4 } };
        System.out.println("\n\n2D Array:");
        for (int i = 0; i < arr2D.length; i++) {
            for (int j = 0; j < arr2D[i].length; j++) {
                System.out.print(arr2D[i][j] + " ");
            }
            System.out.println();
        }

        // Multi-Dimensional Array
        int[][][] arr3D = { { { 1, 2 }, { 3, 4 } }, { { 5, 6 }, { 7, 8 } } };
        System.out.println("\n3D Array:");
        for (int[][] twoD : arr3D) {
            for (int[] oneD : twoD) {
                for (int num : oneD) {
                    System.out.print(num + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
}
