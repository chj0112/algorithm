import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        char[] c = new char[a];
        for (int i = 0; i < a; i++) {
            c[i] = '*';
        }
        for (int j = 0; j < b; j++) {
            System.out.println(c);
        }
    }
}