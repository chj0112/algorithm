import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        StringBuffer sb = new StringBuffer(s);
        String reverseString = sb.reverse().toString();
        if (reverseString.equals(s)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}