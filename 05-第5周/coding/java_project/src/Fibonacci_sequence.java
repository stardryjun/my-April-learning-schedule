public class Fibonacci_sequence {
    public static void main(String[] args) {
        int n = 9;
        int first = 1;
        int second = 1;
        if(n < 0) {
            System.out.println("n must be positive");
            return;
        }
        if(n < 2){
            System.out.println(first);
            return;
        }
        for(int i = 2; i < n; i++) {
            second = first + second;
            first = second - first;
        }
        System.out.println(second);
    }
}
