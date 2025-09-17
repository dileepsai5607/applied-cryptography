import java.util.Random;
import java.util.Scanner;

public class RandomSubsetString {
    public static void main(String[] args) {
        // Take subset input from user
        try (Scanner sc = new Scanner(System.in)) {
            // Take subset input from user
            System.out.print("Enter subset of digits/alphabets: ");
            String subset = sc.nextLine();
            
            // Take length input from user
            System.out.print("Enter length of random string: ");
            int length = sc.nextInt();
            
            String randomString = generateRandomString(subset, length);
            
            System.out.println("Generated Random String: " + randomString);
        }
    }

    // Function to generate random string from subset
    public static String generateRandomString(String subset, int length) {
        Random random = new Random();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(subset.length());
            sb.append(subset.charAt(index));
        }
        return sb.toString();
    }
}
