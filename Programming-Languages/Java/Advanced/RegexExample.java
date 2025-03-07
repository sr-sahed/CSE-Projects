import java.util.regex.*;

public class RegexExample {
    public static void main(String[] args) {
        String pattern = ".*@gmail\\.com";
        String email = "example@gmail.com";

        System.out.println(email.matches(pattern)); // Output: true
    }
}
