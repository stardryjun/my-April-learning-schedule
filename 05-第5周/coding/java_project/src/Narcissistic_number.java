
public class Narcissistic_number {
    public static void main(String[] args) {
        int n = 1000;
        for (int i = 1; i < n; i++) {
            int sum = 0;
            int j = i;
            while (j > 0) {
                sum += (j%10)*(j%10)*(j%10);
                j = j/10;
            }
            if (sum == i) {
                System.out.println(i);
            }
        }
    }
}
