import java.io.*;

public class FileHandlingExample {
    public static void main(String[] args) {
        // Write to File
        try (FileWriter writer = new FileWriter("test.txt")) {
            writer.write("Hello, Java File Handling!");
        } catch (IOException e) {
            System.out.println("Error Writing File");
        }

        // Read from File
        try (BufferedReader reader = new BufferedReader(new FileReader("test.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Read: " + line);
            }
        } catch (IOException e) {
            System.out.println("Error Reading File");
        }
    }
}
