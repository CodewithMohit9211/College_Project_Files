import java.util.Scanner;
public class AddBinary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first binary number: ");
        String b1 = sc.nextLine();
        System.out.print("Enter second binary number: ");
        String b2 = sc.nextLine();
        int num1 = Integer.parseInt(b1, 2);
        int num2 = Integer.parseInt(b2, 2);
        int sum = num1 + num2;
        System.out.println("Sum of binary numbers: " + Integer.toBinaryString(sum));
    }
}