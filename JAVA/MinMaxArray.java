import java.util.Arrays;

public class MinMaxArray {
    public static void main(String[] args) {
        int[] arr = {12, 5, 8, 20, 7};
        Arrays.sort(arr);
        System.out.println("Smallest:" + arr[0]);
        System.out.println("Largest:" + arr[arr.length - 1]);
    }
}