public class SumOfDigits {
    public static long sumDigits(char[] digits) {
        long sum = 0;
        for (char c : digits) {
            if (Character.isDigit(c)) {
                sum += Character.getNumericValue(c);
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        char[] input = {'1', '2', '3', '4', '5'};
        System.out.println("Sum of digits:" + sumDigits(input));
    }
}