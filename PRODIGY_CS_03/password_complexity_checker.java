import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PasswordStrengthChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a password to check its strength: ");
        String password = scanner.nextLine();
        
        String result = checkPasswordStrength(password);
        System.out.println(result);
        
        scanner.close();
    }

    public static String checkPasswordStrength(String password) {
        if (password == null || password.isEmpty()) {
            return "Password cannot be empty.";
        }
        
        int length = password.length();
        boolean hasUpperCase = !password.equals(password.toLowerCase());
        boolean hasLowerCase = !password.equals(password.toUpperCase());
        boolean hasDigit = password.matches(".\\d.");
        boolean hasSpecialChar = password.matches(".[!@#$%^&()_+\\-=\\[\\]{};':\"\\|,.<>/?].*");

        StringBuilder feedback = new StringBuilder();
        
        if (length < 8) {
            feedback.append("Password is too short. ");
        } else if (length <= 12) {
            feedback.append("Password length is acceptable. ");
        } else {
            feedback.append("Password length is good. ");
        }
        
        if (!hasUpperCase) {
            feedback.append("Include at least one uppercase letter. ");
        }
        
        if (!hasLowerCase) {
            feedback.append("Include at least one lowercase letter. ");
        }
        
        if (!hasDigit) {
            feedback.append("Include at least one digit. ");
        }
        
        if (!hasSpecialChar) {
            feedback.append("Include at least one special character. ");
        }
        
        if (feedback.length() == 0) {
            return "Password is strong!";
        } else {
            return feedback.toString();
        }
    }
}
