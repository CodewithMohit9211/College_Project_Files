import java.util.Scanner;
public class CountElements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = sc.nextLine();
        int letters = 0, spaces = 0, numbers = 0, others = 0;
        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) letters++;
            else if (Character.isDigit(c)) numbers++;
            else if (Character.isSpaceChar(c)) spaces++;
            else others++;
        }
        System.out.println("Letters: " + letters);
        System.out.println("Spaces: " + spaces);
        System.out.println("Numbers: " + numbers);
        System.out.println("Other characters: " + others);
    }
}